from datetime import datetime
def test():
    
    print("Le test est né aujourd'hui")
    if calculer_age_jours(10,12,2023,10,12,2023)==0:
        print("C clean ;)")
    else:
        print("C pas bon  :(")
        print("coup dur pour Guillaume")
    
    print("Le test est né demain")
    if calculer_age_jours(28,11,2023,27,11,2023)==None:
        print("C clean ;)")
    else:
        print("C pas bon  :(")
        print("coup dur pour Guillaume")

    print("Le test est né hier")
    if calculer_age_jours(26,12,2023,27,12,2023)==1:
        print("C clean ;)")
    else:
        print("C pas bon  :(")
        print("coup dur pour Guillaume")
        
    print("Le test est né hier, mais le mois dernier")
    if calculer_age_jours(30,11,2023,1,12,2023)==1:
        print("C clean ;)")
    else:
        print("C pas bon  :(")
        print("coup dur pour Guillaume")
        
    print("Le test est né hier, mais l\'année dernière")
    if calculer_age_jours(31,12,2022,1,1,2023)==1:
        print("C clean ;)")
    else:
        print("C pas bon  :(")
        print("coup dur pour Guillaume")
        
    print("Le test est né il y a un mois")
    if calculer_age_jours(1,12,2023,1,1,2024)==31:
        print("C clean ;)")
    else:
        print("C pas bon  :(")
        print("coup dur pour Guillaume")
        
    print("Le test est né il y a un an ,bisextille")
    if calculer_age_jours(1,1,2004,1,1,2005)==366:
        print("C clean ;)")
    else:
        print("C pas bon  :(")
        print("coup dur pour Guillaume")
        
    print("Le test est né il y a un an ,non bisextille")
    if calculer_age_jours(1,1,2005,1,1,2006)==365:
        print("C clean ;)")
    else:
        print("C pas bon  :(")
        print("coup dur pour Guillaume")

# on veut savoir si l'année est bisextille ou pas
def bisextile(a):
    if a % 4 == 0 and a % 100 != 0:
        return True
    return False

# on veut savoir combien y a-t-il de jours dans tel mois de telle année
def jours_dans_mois(m, a):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    if m == 2 and bisextile(a):
        return 29
    if m == 2 and not bisextile(a):
        return 28
    raise ValueError('Heu, mon reuf,j\'avais pas prévu ça')


# c'est le moteur pour calculer le nombre de jours entre 2 dates
def calculer_age_jours(j, m, a, j_a, m_a, a_a):
    
    # on regarde si la date de naissance est avant la date d'aujourd'hui
    indice_date_naiss=a*12*31+m*31+j
    indice_date_aujour=a_a*12*31+m_a*31+j_a
    if indice_date_naiss>indice_date_aujour:
        print('Heu, d\'où t\'es né après aujourd\'hui ?')
        return None
    
    # pour chaque année
    j_f=0
    for a_cours in range(a,a_a+1):
        # si c'est l'année de naissance
        m_depart=1
        if a_cours==a:
            m_depart=m
        m_fin=12
        if a_cours==a_a:
            m_fin=m_a
        # pour chaque mois
        for m_cours in range(m_depart,m_fin+1):
            j_depart=1
            # si c'est le premier mois de la première année
            if a_cours==a and m_cours==m:
                j_depart=j
            j_fin=jours_dans_mois(m_cours,a_cours)
            # si c'est le dernier mois de la dernière année
            if a_cours==a_a and m_cours==m_a:
                j_fin=j_a
            # on ajoute le nombre de jour dans ce mois
            j_f=j_f+(j_fin-j_depart+1)
            
    # on enleve le jour d'aujourd'hui  
    return j_f-1
    
# c'est la fonction principale
def calculer_age(j, m, a):
    
    # on cherche la date du jour
    now = datetime.now()
    j_a=int(now.strftime("%d"))
    m_a=int(now.strftime("%m"))
    a_a=int(now.strftime("%Y"))
    
    heures_par_jour = 24
    minutes_par_heure = 60
    secondes_par_minute = 60

    jours_age = calculer_age_jours(j,m,a,j_a,m_a,a_a)
    if jours_age==None:
        return None
    
    # on calcule l'age en années
    annee_age = a_a - a - 1
    # est-ce que son anniverssaire est déjà passé
    if m_a>m or (m_a==m and j_a>=j):
        # dans ce cas là on ajoute un an
        annee_age = annee_age + 1
        # et on defini une variable qui va nous servir plus tard
        prochain_anniv_cette_annee=1
    else:
        prochain_anniv_cette_annee=0

    # on calcule son age en mois
    mois_age = (a_a - a) * 12 + m_a - m

    # en heures
    heures_age = jours_age * heures_par_jour
    
    # en minutes
    minutes_age = heures_age*minutes_par_heure
    
    # en secondes
    secondes_age = minutes_age * secondes_par_minute

    # on cherche dans conbien de temps est son anniversaire
    if prochain_anniv_cette_annee==1:
        a_p=a_a+1
    else:
        a_p=a_a
    prochain_anniv_jours=calculer_age_jours(j_a,m_a,a_a,j,m,a_p)
    if m<m_a:
        prochain_mois = m - m_a + 12
    elif m==m_a and j<j_a:
        prochain_mois = m - m_a + 11
    else:
        prochain_mois = m - m_a
    # les jours
    if j>=j_a:
        prochain_jours = j - j_a
    else:
        prochain_jours = j - j_a + 30
    # on affiche tout ça
    print("Ton âge en :")
    print("en annees:",annee_age)
    print("en mois:",mois_age)
    print("en jours:",jours_age)
    print("en heures:",heures_age)
    print("en minutes:",minutes_age)
    print("en secondes:",secondes_age)
    # on regarde si son anniverssaire est aujourd'hui
    if prochain_jours!=0 and prochain_mois!=0:
        print("Ton prochain anniv est dans")
        print(prochain_anniv_jours,"jours")
    elif m==m_a and j==j_a:
        print("Joyeux Anniversaire ;)")