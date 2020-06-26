import argparse

import pandas as pd
from ska_sdc import Sdc1Scorer

from utils import CAT_COLUMNS, GAUL_COLUMNS, SRL_COLUMNS


def score_from_srl(srl_path, truth_path, freq, verbose=False):
    """
    Given source list output by PyBDSF and training truth catalogue,
    calculate the official score for the sources identified in the srl.

    Args:
        srl_path (`str`): Path to source list (.srl file)
        truth_path (`str`): Path to training truth catalogue
        freq (`int`): Image frequency band (560, 1400 or 9200 MHz)
        verbose (`bool`): True to print out size ratio info
    """
    truth_df = load_truth_df(truth_path)

    # Predict size ID and correct the Maj and Min values:
    cat_df = cat_df_from_srl(srl_path)

    scorer = Sdc1Scorer(cat_df, truth_df, freq)
    score = scorer.run(train=True, detail=True, mode=1)

    return score


def load_truth_df(truth_path):
    """
    Load the training area truth catalogue.
    Expected to be in the format as provided on the SDC1 website.

    Args:
        truth_path (`str`): Path to training truth catalogue
    """
    truth_df = pd.read_csv(
        truth_path,
        skiprows=18,
        names=CAT_COLUMNS,
        usecols=range(12),
        delim_whitespace=True,
    )
    return truth_df


def srl_as_df(srl_path):
    """
    Load the source list output by PyBDSF as a pd.DataFrame

    Args:
        srl_path (`str`): Path to source list (.srl file)
    """
    srl_df = pd.read_csv(
        srl_path, skiprows=6, names=SRL_COLUMNS, delim_whitespace=True,
    )
    return srl_df


def gaul_as_df(gaul_path):
    """
    Load the Gaussian list output by PyBDSF as a pd.DataFrame

    Args:
        gaul_path (`str`): Path to Gaussian list (.srl file)
    """
    gaul_df = pd.read_csv(
        gaul_path, skiprows=6, names=GAUL_COLUMNS, delim_whitespace=True,
    )
    return gaul_df


def cat_df_from_srl(srl_path):
    """
    Load the source list output by PyBDSF and create a catalogue DataFrame of the
    form required for SDC1.

    Args:
        srl_path (`str`): Path to source list (.srl file)
    """
    srl_df = srl_as_df(srl_path)

    # Instantiate catalogue DataFrame
    cat_df = pd.DataFrame()

    # Source ID
    cat_df["id"] = srl_df["Source_id"]

    # Positions (correct RA degeneracy to be zero)
    cat_df["ra_core"] = srl_df["RA_max"]
    cat_df.loc[cat_df["ra_core"] > 180.0, "ra_core"] -= 360.0
    cat_df["dec_core"] = srl_df["DEC_max"]

    cat_df["ra_cent"] = srl_df["RA"]
    cat_df.loc[cat_df["ra_cent"] > 180.0, "ra_cent"] -= 360.0
    cat_df["dec_cent"] = srl_df["DEC"]

    # Flux and core fraction
    cat_df["flux"] = srl_df["Total_flux"]
    cat_df["core_frac"] = (srl_df["Peak_flux"] - srl_df["Total_flux"]).abs()

    # Bmaj, Bmin (convert deg -> arcsec) and PA
    # Source list outputs FWHM as major/minor axis measures
    cat_df["b_maj"] = srl_df["Maj"] * 3600
    cat_df["b_min"] = srl_df["Min"] * 3600
    cat_df["pa"] = srl_df["PA"]

    # Size class
    cat_df["size"] = 2

    # Class
    # TODO: To be predicted using classifier
    cat_df["class"] = 1
    return cat_df


def srl_gaul_df(gaul_path, srl_path):
    """
    Given a gaussian list (.gaul) and source list (.srl) from PyBDSF, return a
    catalogue of sources, including the number of components.
    """
    gaul_df = gaul_as_df(gaul_path)
    srl_df = srl_as_df(srl_path)

    srl_df["n_gaussians"] = gaul_df["Source_id"].value_counts()

    return srl_df


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s", help="Path to source list (.srl) output by PyBDSF", type=str
    )
    parser.add_argument("-t", help="Path to truth training catalogue", type=str)
    parser.add_argument(
        "-f", help="Image frequency band (560||1400||9200, MHz)", default=1400, type=int
    )
    # parser.add_argument(
    #     "-g", help="Path to gaussian list (.gaul) output by PyBDSF", type=str
    # )
    args = parser.parse_args()

    score = score_from_srl(args.s, args.t, args.f, verbose=True)
    print("Score was {}".format(score.value))
    print("Number of detections {}".format(score.n_det))
    print("Number of matches {}".format(score.n_match))
    print("Number of matches that were too far from truth {}".format(score.n_bad))
    print("Number of false detections {}".format(score.n_false))
    print("Score for all matches {}".format(score.score_det))
    print("Accuracy percentage {}".format(score.acc_pc))
