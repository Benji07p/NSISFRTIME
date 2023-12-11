from datetime import datetime

# L'année rentrée est-elle bissextile ?
def bissextile(a):
    if a % 4 == 0 and a % 100 != 0:
        return True
    return False

# Attribution des jours par rapport au mois
def jours_dans_mois(m, a):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    if m == 2 and bissextile(a):
        return 29
    if m == 2 and not bissextile(a):
        return 28
    raise ValueError('Erreur de valeur')


# Calculer le nombre de jours entre 2 dates
def calculer_nombre_jours(j, m, a, j_a, m_a, a_a):
    
    # La date de naissance est-elle avant la date d'aujourd'hui ?
    indice_date_naiss=a*12*31+m*31+j
    indice_date_aujour=a_a*12*31+m_a*31+j_a
    if indice_date_naiss>indice_date_aujour:
        print("Vous ne pouvez pas rentrez une date après aujourd'hui !")
        return None
    
    # Pour chaque année :
    j_f=0
    for a_cours in range(a,a_a+1):
        # Si c'est l'année de naissance
        m_depart=1
        if a_cours==a:
            m_depart=m
        m_fin=12
        if a_cours==a_a:
            m_fin=m_a
        # Pour chaque mois :
        for m_cours in range(m_depart,m_fin+1):
            j_depart=1
            # Si c'est le premier mois de la première année :
            if a_cours==a and m_cours==m:
                j_depart=j
            j_fin=jours_dans_mois(m_cours,a_cours)
            # Si c'est le dernier mois de la dernière année :
            if a_cours==a_a and m_cours==m_a:
                j_fin=j_a
            # Ajouter le nombre de jour dans ce mois
            j_f=j_f+(j_fin-j_depart+1)
            
    # Soustraire aujourd'hui  
    return j_f-1
    
# Fonction Principale
def calculer_age(j, m, a):
    
    # Attribuer la date du jour
    now = datetime.now()
    j_a=int(now.strftime("%d"))
    m_a=int(now.strftime("%m"))
    a_a=int(now.strftime("%Y"))

    # Liste des constantes importantes
    heures_par_jour = 24
    minutes_par_heure = 60
    secondes_par_minute = 60

    jours_age = calculer_nombre_jours(j,m,a,j_a,m_a,a_a)
    if jours_age==None:
        return None
    
    # Age en année
    annee_age = a_a - a - 1
    # Anniversaire est-il déjà passé ?
    if m_a>m or (m_a==m and j_a>=j):
        # Si oui, rajouter une année
        annee_age = annee_age + 1
        anniv_deja_pass=True
    else:
        anniv_deja_pass=False

    # Calculer l'age en mois
    mois_age = (a_a - a) * 12 + m_a - m

    # Calculer l'age en heures
    heures_age = jours_age * heures_par_jour
    
    # Calculer l'age en minutes
    minutes_age = heures_age * minutes_par_heure
    
    # Calculer l'age en secondes
    secondes_age = minutes_age * secondes_par_minute

    # Calculer dans combien de temps arrive son anniversaire
    a_p=a_a
    if anniv_deja_pass:
        a_p=a_p+1
    prochain_anniv_jours=calculer_nombre_jours(j_a,m_a,a_a,j,m,a_p)
    
    if m<m_a:
        prochain_mois_mois = m - m_a + 12
    elif m==m_a and j<j_a:
        prochain_mois_mois = m - m_a + 11
    else:
        prochain_mois_mois = m - m_a
    
    # Calculer les jours
    # EN TRAVAUX
    '''prochain_mois_jours=calculer_nombre_jours(j_a,m-1,a_p,j,m,a_p)+1'''
    
    # Afficher tous les résultats
    print("Ton âge en :")
    print("annees:",annee_age)
    print("mois:",mois_age)
    print("jours:",jours_age)
    print("heures:",heures_age)
    print("minutes:",minutes_age)
    print("secondes:",secondes_age)
    # Anniversaire ?
    if prochain_mois_mois!=0 or prochain_mois_jours!=0:
        print("Ton prochain anniversaire est dans")
        print(prochain_anniv_jours,"jours")
        if prochain_mois_mois!=0:
            print("ou",prochain_mois_mois,"mois")
            if prochain_mois_jours!=0:
                print("et",prochain_mois_jours,"jours")
    elif m==m_a and j==j_a:
        print("Joyeux Anniversaire")
