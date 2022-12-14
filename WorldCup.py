
# from easygui import *
import easygui
import random
import sys

beginIMG = "./images/imageWorldCup.gif"
winnerIMG = "./images/FIFA-World-Cup-Winner.gif"

groupA = ["Qatar", "Ecuador", "Senegal", "Netherlands"]
groupB = ["England", "Iran", "USA", "Wales"]
groupC = ["Argentina", "Saudi Arabia", "Mexico", "Poland"]
groupD = ["France", "Australia", "Denmark", "Tunisia"]
groupE = ["Spain", "Costa Rica", "Germany", "Japan"]
groupF = ["Belgium", "Canada", "Morocco", "Croatia"]
groupG = ["Brazil", "Serbia", "Switzerland", "Cameroon"]
groupH = ["Portugal", "Ghana", "Uruguay", "South Korea"]

def QuarterFinals():

    global Aquarter, Bquarter, Cquarter, Dquarter, Equarter, Fquarter, Gquarter, Hquarter, semi1Full, semi2Full, semi3Full, semi4Full

    msg = (
        "Quarter-Finals\n\n\n"
        + str(Aquarter).upper()
        + str(" vs ")
        + str(Bquarter).upper()
        + str("\n\n")
        + str(Cquarter).upper()
        + str(" vs ")
        + str(Dquarter).upper()
        + str("\n\n")
        + str(Equarter).upper()
        + str(" vs ")
        + str(Fquarter).upper()
        + str("\n\n")
        + str(Gquarter).upper()
        + str(" vs ")
        + str(Hquarter).upper()
    )
    choices = ["Semi-finals"]
    reply = easygui.buttonbox(msg, choices=choices)
    if reply == "Semi-finals":
        semiFinals()
    else:
        sys.exit(0)


def winners():
    global winner

    winner = winner[0]

    msg = "             WINNER OF FIFA WORLD CUP 2022 IS:  " + str(winner).upper() + " !!!"
    choices = ["OK"]
    reply = easygui.buttonbox(msg, image=winnerIMG, choices=choices)
    sys.exit(0)


def finals():
    global final1full, final2full, win1final, win2final

    msg = "Final\n\n\n" + str(win1final) + str(" vs ") + str(win2final)
    choices = ["Winner"]
    reply = easygui.buttonbox(msg, choices=choices)
    if reply == "Winner":
        winners()
    else:
        sys.exit(0)


def semiFinals():
    global semi1Full, semi2Full, semi3Full, semi4Full, semi1win, semi2win, semi3win, semi4win

    msg = (
        "Semi-Finals\n\n\n"
        + str(semi1win).upper()
        + str(" vs ")
        + str(semi2win).upper()
        + str("\n")
        + str(semi3win).upper()
        + str(" vs ")
        + str(semi4win).upper()
    )
    choices = ["Finals"]
    reply = easygui.buttonbox(msg, choices=choices)
    if reply == "Finals":
        finals()
    else:
        sys.exit(0)


def roundOf16():

    global AFull, BFull, CFull, DFull, EFull, GFull, HFull, Aquarter, Bquarter, Cquarter, Dquarter, Equarter, Fquarter, Gquarter, Hquarter, semi1Full, semi2Full, semi3Full, semi4Full, semi1win, semi2win, semi3win, semi4win, final1full, final2full, win1final, win2final, winner

    random.shuffle(groupA)
    random.shuffle(groupB)
    random.shuffle(groupC)
    random.shuffle(groupD)
    random.shuffle(groupE)
    random.shuffle(groupF)
    random.shuffle(groupG)
    random.shuffle(groupH)

    A1roundOf16 = groupA[0]
    A2roundOf16 = groupA[1]
    B1roundOf16 = groupB[0]
    B2roundOf16 = groupB[1]
    C1roundOf16 = groupC[0]
    C2roundOf16 = groupC[1]
    D1roundOf16 = groupD[0]
    D2roundOf16 = groupD[1]
    E1roundOf16 = groupE[0]
    E2roundOf16 = groupE[1]
    F1roundOf16 = groupF[0]
    F2roundOf16 = groupF[1]
    G1roundOf16 = groupG[0]
    G2roundOf16 = groupG[1]
    H1roundOf16 = groupH[0]
    H2roundOf16 = groupH[1]

    AFull = [groupA[0], groupB[1]]
    BFull = [groupC[0], groupD[1]]
    CFull = [groupE[0], groupF[1]]
    DFull = [groupG[0], groupH[1]]
    EFull = [groupB[0], groupA[1]]
    FFull = [groupD[0], groupC[1]]
    GFull = [groupF[0], groupE[1]]
    HFull = [groupH[0], groupG[1]]

    random.shuffle(AFull)
    random.shuffle(BFull)
    random.shuffle(CFull)
    random.shuffle(DFull)
    random.shuffle(EFull)
    random.shuffle(FFull)
    random.shuffle(GFull)
    random.shuffle(HFull)

    Aquarter = AFull[0]
    Bquarter = BFull[0]
    Cquarter = CFull[0]
    Dquarter = DFull[0]
    Equarter = EFull[0]
    Fquarter = FFull[0]
    Gquarter = GFull[0]
    Hquarter = HFull[0]

    semi1Full = [Aquarter, Bquarter]
    semi2Full = [Cquarter, Dquarter]
    semi3Full = [Equarter, Fquarter]
    semi4Full = [Gquarter, Hquarter]

    random.shuffle(semi1Full)
    random.shuffle(semi2Full)
    random.shuffle(semi3Full)
    random.shuffle(semi4Full)

    semi1win = semi1Full[0]
    semi2win = semi2Full[0]
    semi3win = semi3Full[0]
    semi4win = semi4Full[0]

    final1full = [semi1win, semi2win]
    final2full = [semi3win, semi4win]

    random.shuffle(final1full)
    random.shuffle(final2full)

    win1final = final1full[0]
    win2final = final2full[0]

    winner = [win1final, win2final]
    random.shuffle(winner)

    msg = (
        "Round of 16\n\n\n"
        + str("A1 ")
        + str(A1roundOf16).upper()
        + str(" vs ")
        + str("B2 ")
        + str(B2roundOf16).upper()
        + str("\n\nC1 ")
        + str(C1roundOf16).upper()
        + str(" vs ")
        + str("D2 ")
        + str(D2roundOf16).upper()
        + str("\n\nE1 ")
        + str(E1roundOf16).upper()
        + str(" vs ")
        + str("F2 ")
        + str(F2roundOf16).upper()
        + str("\n\nG1 ")
        + str(G1roundOf16).upper()
        + str(" vs ")
        + str("H2 ")
        + str(H2roundOf16).upper()
        + str("\n\nB1 ")
        + str(B1roundOf16).upper()
        + str(" vs ")
        + str("A2 ")
        + str(A2roundOf16).upper()
        + str("\n\nD1 ")
        + str(D1roundOf16).upper()
        + str(" vs ")
        + str("C2 ")
        + str(C2roundOf16).upper()
        + str("\n\nF1 ")
        + str(F1roundOf16).upper()
        + str(" vs ")
        + str("E2 ")
        + str(E2roundOf16).upper()
        + str("\n\nH1 ")
        + str(H1roundOf16).upper()
        + str(" vs ")
        + str("G2 ")
        + str(G2roundOf16).upper()
    )
    choices = ["Quarter-finals"]
    reply = easygui.buttonbox(msg, choices=choices)
    if reply == "Quarter-finals":
        QuarterFinals()
    else:
        sys.exit(0)


def main():

    msg = (
        "ALL THE WORLD CUP TEAMS:\n\n"
        + str("Group A:\n")
        + str(
            (groupA[0]).upper()
            + str(", ")
            + str(groupA[1]).upper()
            + str(", ")
            + str(groupA[2]).upper()
            + str(", ")
            + str(groupA[3]).upper()
        )
        + str("\n\nGroup B:\n")
        + str(groupB[0].upper())
            + str(", ")
            + str(groupB[1]).upper()
            + str(", ")
            + str(groupB[2]).upper()
            + str(", ")
            + str(groupB[3]).upper()
        
        + str("\n\nGroup C:\n")
        + str(
            (groupC[0].upper())
            + str(", ")
            + str(groupC[1]).upper()
            + str(", ")
            + str(groupC[2]).upper()
            + str(", ")
            + str(groupC[3]).upper()
        )
        + str("\n\nGroup D:\n")
        + str(
            (groupD[0].upper())
            + str(", ")
            + str(groupD[1]).upper()
            + str(", ")
            + str(groupD[2]).upper()
            + str(", ")
            + str(groupD[3]).upper()
        )
        + str("\n\nGroup E:\n")
        + str(
            (groupE[0].upper())
            + str(", ")
            + str(groupE[1]).upper()
            + str(", ")
            + str(groupE[2]).upper()
            + str(", ")
            + str(groupE[3]).upper()
        )
        + str("\n\nGroup F:\n")
        + str(
            (groupF[0].upper())
            + str(", ")
            + str(groupF[1]).upper()
            + str(", ")
            + str(groupF[2]).upper()
            + str(", ")
            + str(groupF[3]).upper()
        )
        + str("\n\nGroup G:\n")
        + str(
            (groupG[0].upper())
            + str(", ")
            + str(groupG[1].upper())
            + str(", ")
            + str(groupG[2].upper())
            + str(", ")
            + str(groupG[3].upper())
        )
        + str("\n\nGroup H:\n")
        + str(
            (groupH[0].upper())
            + str(", ")
            + str(groupH[1]).upper()
            + str(", ")
            + str(groupH[2]).upper()
            + str(", ")
            + str(groupH[3]).upper()
        )
    )
    choices = ["Begin the World Cup!!!"]
    reply = easygui.buttonbox(msg, image=beginIMG, choices=choices)
    if reply == "Begin the World Cup!!!":
        roundOf16()
    elif reply == "./images/imageWorldCup.gif":
        roundOf16()
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
