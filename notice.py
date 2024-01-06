
# ========== CREATION D'UN ENVIRONNEMENT VIRTUEL PYTHON =====================

#création d'un environnement virtuel python avec la commande : python -m venv venv

#activer l'environnement virtuel en utilisant la commande : venv\Scripts\activate 

#si y'a message d'erreur qui indique que vous ne pouvez pas exécuter le script d'activation de l'environnement virtuel (Activate.ps1) c'est en raison des paramètres de politique 
#d'exécution de scripts sur votre système. Ceci est un mécanisme de sécurité dans PowerShell.

#Pour résoudre ce problème, vous pouvez ajuster la politique d'exécution des scripts pour permettre l'exécution de scripts locaux (comme le script d'activation de l'environnement virtuel). 
#Voici comment vous pouvez le faire :

# 1. Ouvrez PowerShell en tant qu'administrateur : Recherchez "PowerShell" dans le menu Démarrer, faites un clic droit sur "Windows PowerShell" et sélectionnez "Exécuter en tant qu'administrateur".

# 2. Vérifiez la politique d'exécution actuelle : Dans la fenêtre PowerShell, exécutez la commande suivante pour vérifier la politique d'exécution actuelle : Get-ExecutionPolicy
# on observe restricted 

# 3. Changez la politique d'exécution : Si la politique actuelle est restrictive (par exemple, "Restricted" ou "AllSigned"), vous pouvez la changer en "RemoteSigned" 
#qui permet l'exécution de scripts locaux. Utilisez la commande suivante pour changer la politique : Set-ExecutionPolicy RemoteSigned

# 4. Exécutez le script d'activation : Essayez à nouveau d'exécuter le script d'activation de l'environnement virtuel : venv\Scripts\Activate

# Maintenant, vous devriez être en mesure d'activer l'environnement virtuel sans rencontrer l'erreur de politique d'exécution.

# !!!N'oubliez pas que modifier la politique d'exécution des scripts peut avoir des implications en termes de sécurité, donc faites attention aux scripts que vous exécutez!!!
#Une fois que vous avez terminé avec votre environnement virtuel, vous pouvez rétablir la politique d'exécution par défaut en exécutant : Set-ExecutionPolicy Default
#ainsi il sera remis en restricted

#nb:
#Lorsque vous activez l'environnement virtuel à l'intérieur du dossier de votre projet, vous travaillez avec une instance isolée de Python qui est spécifique à ce projet. 
#Cela signifie que toutes les dépendances que vous installez (comme Streamlit) sont installées dans cet environnement virtuel et n'affectent pas l'installation globale de Python sur votre 
#système. Lorsque l'environnement virtuel est activé, toutes les commandes que vous exécutez (comme l'exécution de Streamlit) utilisent l'interpréteur Python de l'environnement virtuel, 
#et les packages que vous avez installés à l'intérieur de cet environnement virtuel sont utilisés.

#Une fois l'environnement virtuel activé, le nom de l'environnement virtuel sera affiché dans l'invite de commande, indiquant que vous travaillez dans cet environnement.

#À tout moment, lorsque vous avez terminé de travailler sur votre projet ou que vous souhaitez quitter l'environnement virtuel, vous pouvez simplement taper la commande : deactivate
#Cela vous ramènera à l'environnement Python global de votre système.

#Il est important de noter que lorsque vous quittez le terminal ou fermez VS Code, l'environnement virtuel sera automatiquement désactivé. N'oubliez pas de changer aussi la politique d'exec.
#Lorsque vous rouvrez un terminal dans le même dossier de projet, vous devrez réactiver l'environnement virtuel si vous souhaitez continuer à travailler à l'intérieur de celui-ci.
#L'utilisation d'environnements virtuels est utile pour isoler les dépendances et les packages d'un projet à l'autre, ce qui peut être très pratique lorsque vous travaillez sur 
#plusieurs projets en même temps. Cela vous permet également de gérer les versions des packages spécifiques à chaque projet sans interférer avec d'autres projets ou installations globales.
#plusieurs avantages : isolation des projets, gestion des dép, portabilité(on peut partager l'env virtuel et d'autres avec le fichier requirements.txt), env propre(quand on quitte l'env virt.
#le systeme revient à l'installation de python globale), facilité de gestion(faciliter à activer/desactiver l'environnement virtuel)

#Vous pouvez créer un environnement virtuel même sur un ordinateur où Python n'est pas installé globalement. L'environnement virtuel contient sa propre copie de l'interpréteur Python 
#ainsi que les outils nécessaires, y compris pip, pour installer des packages spécifiques à ce projet.

# =============================================================================


#commande : pip install streamlit (donc streamlit s'installe à l'interieur de l'environnement virtuel)
#commande : streamlit hello pour voir si tout va bien 
#commande : streamlit run nomfichier.py pour lancer dans le navigateur

import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

st.write("Hello World!")

data = np.random.normal(size=1000)
data = pd.DataFrame(data, columns=["Dist_norm"])
st.write(data.head())
# or st.dataframe(data.head()) pour afficher un dataframe

#creation d'un graphique avec matplotlib

#plt.hist(data.Dist_norm)
#plt.show #rien ne s'affiche car streamlit a des fonctions dédiés qui fonctionnent avec des librairies comme mtlp seaborn etc
#st.pyplot()
#s'affiche mais y'a un warning car besoin d'un argument qui represente la figure en question et propose un code donc on le met

fig, ax = plt.subplots()
ax.hist(data.Dist_norm)
st.pyplot(fig)