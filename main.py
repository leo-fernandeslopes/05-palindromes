""" Dans main.py, on code la fonction ispalindrome(p) et ses tests automatiques. """
#### Fonction secondaire

def ispalindrome(p):
    """
    Elle prend en paramètre une String p et renvoie un booléen qui
    affirme si p est un palindrome.
    """

    p = p.lower()

    accents = "àâäéèêëîïôöùûüÿç-',;.?:!_"
    sans_accents = "aaaeeeeiioouuuyc         "

    dico = str.maketrans(accents, sans_accents)
    p = p.translate(dico).replace(" ", "")
    return p == p[::-1]

#### Fonction principale


def main():
    """
    La procédure ne prend aucun paramètre et effectue les tests de palindrome(p). """

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
