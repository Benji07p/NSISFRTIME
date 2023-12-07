from datetime import datetime
def test():
  
  if calculer_age_jours(27,11,2007,30,11,2023)==5845:
    print("C clean ;)")
  else:
    print("C pas bon  :(")
    print("coup dur pour Guillaume")

  if calculer_age_jours(27,11,2007,27,11,2023)==5842:
    print("C clean ;)")
  else:
    print("C pas bon  :(")
    print("coup dur pour Guillaume")
  
  if calculer_age_jours(27,11,2007,27,10,2023)==5811:
    print("C clean ;)")
  else:
    print("C pas bon  :(")
    print("coup dur pour Guillaume")
    
  if calculer_age_jours(27,11,2007,27,12,2023)==5872:
    print("C clean ;)")
  else:
    print("C pas bon  :(")
    print("coup dur pour Guillaume")
  
  if calculer_age_jours(27,11,2007,27,12,2023)==5872:
    print("C clean ;)")
  else:
    print("C pas bon  :(")
    print("coup dur pour Guillaume")

def bisextile(a):
    if a % 4 == 0 and a % 100 != 0:
        return True
    return False

def jours_dans_mois(m, a):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    if m == 2 and bisextile(a):
        return 29
    if m == 2 and not bisextile(a):
        return 28

def calculer_age_jours(j=27, m=11, a=2007, j_a=0, m_a=0, a_a=0):
    
    now = datetime.now()
    if j_a==0:
        j_a=int(now.strftime("%d"))
    if m_a==0: 
        m_a=int(now.strftime("%m"))
    if a_a==0:
        a_a=int(now.strftime("%Y"))
    
    jours=0
    a_en_cours=a
    j_f=0
    while a_a>a_en_cours:
        a_en_cours=a_en_cours+1
        if bisextile(a_en_cours)==True:
            j_f=j_f+366
        elif bisextile(a_en_cours)==False:
            j_f=age*365
    n=0
    soustr_jours=0
    while 1+n<m:
        n=n+1
        soustr_jours=soustr_jours+jours_dans_mois(n,a)
    j_f=j_f-soustr_jours
    t=0
    soust_jours=0
    while 12-t>m_a:
        if jours_dans_mois(m_a,a_a)==
            t=t+1
            soust_jours=soust_jours+jours_dans_mois(12-t,a_a)
        j_f=j_f-soust_jours
    return j_f
    
    
def calculer_age(j=27, m=11, a=2007, j_a=0, m_a=0, a_a=0):

    now = datetime.now()
    if j_a==0:
        j_a=int(now.strftime("%d"))
    if m_a==0: 
        m_a=int(now.strftime("%m"))
    if a_a==0:
        a_a=int(now.strftime("%Y"))
    
    j_s="Vendredi"
    heures_par_jour = 24
    minutes_par_heure = 60
    secondes_par_minute = 60

    jours_age = calculer_age_jours(j,m,a,j_a,m_a,a_a)
    if m_a>m: 
      if j_a>j:
        annee_age = a_a - a - 1
      else:
        annee_age = a_a - a
    elif m_a==m and j_a>j:
      annee_age = a_a - a
    elif m_a==m:
      annee_age = a_a - a
    else:
      annee_age = a_a - a - 1

    mois_age = (a_a - a) * 12 + m_a - m

    heures_age = jours_age * heures_par_jour

    minutes_age = heures_age*minutes_par_heure

    secondes_age = minutes_age * secondes_par_minute

    if m<m_a:
      prochain_mois = m - m_a + 12
    elif m==m_a and j<j_a:
      prochain_mois = m - m_a + 11
    else:
      prochain_mois = m - m_a
    if j>=j_a:
      prochain_jours = j - j_a
    else:
      prochain_jours = j - j_a + 30

    if j_s==1:
      j_s_p=1

    print("en annees:",annee_age)
    print("en mois:",mois_age)
    print("en jours:",jours_age)
    print("en heures:",heures_age)
    print("en minutes:",minutes_age)
    print("en secondes:",secondes_age)
    if prochain_jours!=0:
      if prochain_mois!=0:
        print("ton prochain anniv est dans")
      else:
        print("ton prochain anniv est dans")
    
    if m==m_a and j==j_a:
      print("Joyeux Anniversaire")
    if prochain_mois!=0:
      print(prochain_mois,"mois")
    if prochain_jours!=0:
      print(prochain_jours,"jours")
  