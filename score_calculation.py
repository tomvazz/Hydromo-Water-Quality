import random
import sys
import math


def BOD_Qval(userVal):
    Qval = 0;
    Qval = 97.99742145 * pow(.90138523, userVal);

    return Qval;


def DissolvedO2_Qval(userVal):
    Qval = 0;
    Qval = (
            ((7.5487 * pow(10, -7)) * pow(userVal, 4))
            + ((-3.469409 * pow(10, -4)) * pow(userVal, 3))
            + ((.040307) * pow(userVal, 2))
            + (-.40892345 * userVal)
            + (4.59723));

    return Qval;


def FecalColiform_Qval(userVal):
    Qval = 0;
    Qval = (130.662201 * pow(userVal, -.2710369));
    return Qval;


def Nitrate_Qval(userVal):
    Qval = 0;
    if (userVal <= 10):
        Qval = ((-60 * userVal) + 100);
    else:
        Qval = (79.56047 * pow(.9632, userVal));

    return Qval;


def PH_Qval(userVal):
    Qval = 0;
    if (userVal <= 7.486725):
        Qval = (
                ((-.48107) * pow(userVal, 4))
                + ((8.55765) * pow(userVal, 3))
                + ((-49.79321) * pow(userVal, 2))
                + (121.5186 * userVal)
                + (-104.61758)
        )
    else:
        Qval = (
                ((-1.19277) * pow(userVal, 4))
                + ((47.4707) * pow(userVal, 3))
                + ((-697.79441) * pow(userVal, 2))
                + (4465.56149 * userVal)
                + (-10400.236)
        )
    return Qval;


def Temp_Qval(userVal):
    Qval = 0;
    if (userVal <= 0):
        Qval = ((3.8 * userVal) + 93);
    else:
        Qval = (
                ((-5.804 * pow(10, -4)) * pow(userVal, 4))
                + ((.03353) * pow(userVal, 3))
                + ((-.493065) * pow(userVal, 2))
                + (-2.55718 * userVal)
                + (93.27195)
        )
    return Qval;


def TotalDissolvedSolids_Qval(userVal):
    Qval = 0;
    Qval = (
            ((-4.372 * pow(10, -9)) * pow(userVal, 4))
            + ((5.0328 * pow(10, -6)) * pow(userVal, 3))
            + ((-2.031 * pow(10, -3)) * pow(userVal, 2))
            + (.204644 * userVal)
            + (79.85455)
    )
    return Qval;


def Phosphate_Qval(userVal):
    Qval = 0;
    if (userVal <= 1):
        Qval = ((-60 * userVal) + 100);
    else:
        Qval = (
                ((.01754103) * pow(userVal, 4))
                + ((-.44502) * pow(userVal, 3))
                + ((4.3512) * pow(userVal, 2))
                + (-21.72 * userVal)
                + (57.4007)
        )
    return Qval;


def Turbidity_Qval(userVal):
    Qval = 0;
    Qval = (
            ((1.465 * pow(10, -6)) * pow(userVal, 4))
            + ((-4.04 * pow(10, -4)) * pow(userVal, 3))
            + ((.042296) * pow(userVal, 2))
            + (-2.457 * userVal)
            + (97.4311)
    )
    return Qval;


def weighingFactor(bod_q, do_q, fec_q, nit_q, temp_q, tds_q, phos_q, turb_q, ph_q):
    total_score = 0

    # weightage
    bod_weight = 0.11
    do_weight = 0.17
    fec_weight = 0.16
    nit_weight = 0.10
    temp_weight = 0.10
    tds_weight = 0.07
    phos_weight = 0.10
    turb_weight = 0.08
    ph_weight = 0.11

    total_score = int((bod_q*bod_weight)+(do_q*do_weight)+(fec_q*fec_weight)+(nit_q*nit_weight)+(temp_q*temp_weight)
                      +(tds_q*tds_weight)+(phos_q*phos_weight)+(turb_q*turb_weight)+(ph_q*ph_weight))

    return total_score



def water_quality(score):
    quality = ""
    if (score > 90):
        quality = "excellent"
    elif (score > 70):
        quality = "good"
    elif (score > 50):
        quality = "average"
    elif (score > 25):
        quality = "fair"
    else:
        quality = "poor"

    return quality

# driver retrieves q values and retrieves overall score and returns this score
def driver(bod, do, fec, nit, temp, tds, phos, turb, ph):

    bod_q = BOD_Qval(bod)
    do_q = DissolvedO2_Qval(do)
    fec_q = FecalColiform_Qval(fec)
    nit_q = Nitrate_Qval(nit)
    temp_q = Temp_Qval(temp)
    tds_q = TotalDissolvedSolids_Qval(tds)
    phos_q = Phosphate_Qval(phos)
    turb_q = Turbidity_Qval(turb)
    ph_q = PH_Qval(ph)

    overall_score = weighingFactor(bod_q, do_q, fec_q, nit_q, temp_q, tds_q, phos_q, turb_q, ph_q)

    quality = water_quality(overall_score)

    return overall_score, quality