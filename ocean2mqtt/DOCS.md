# Ocean2MQTT (bêta)

Passerelle EnOcean ↔ MQTT multimarque, façon Zigbee2MQTT. Les produits appairés
apparaissent automatiquement dans Home Assistant grâce à la découverte MQTT.

## Avant de démarrer

1. **Serveur MQTT** : installez et démarrez l'add-on officiel **Mosquitto broker**,
   puis activez l'intégration **MQTT** si Home Assistant la propose. Ocean2MQTT
   récupère tout seul l'adresse et les identifiants de Mosquitto.
2. **Clé EnOcean** : branchez la clé USB (USB 300, USB 500…).
   ⚠️ Une clé ne peut être utilisée que par un seul logiciel à la fois : si
   **NodOcean for HA** utilise la même clé, désactivez cette intégration pendant
   le test (ou utilisez une deuxième clé).

## Vous utilisiez NodOcean for HA ?

Ocean2MQTT reprend vos produits **sans les réappairer** : au premier démarrage, un
bandeau « NodOcean for HA détecté » propose de les reprendre (ou depuis
**Réglages → Migration et sauvegarde**). L'add-on lit la configuration de Home
Assistant en lecture seule.

1. Gardez la **même clé EnOcean** : vos actionneurs la reconnaissent.
2. **Désactivez NodOcean for HA** (Paramètres → Appareils et services → NodOcean for
   HA → ⋮ → Désactiver), puis redémarrez cet add-on : une clé ne peut être utilisée
   que par un seul logiciel.
3. Lancez la reprise : produits, noms, pièces, décalages d'adresse et codes Remote
   Commissioning sont importés.

Vous passez à **une autre clé** ? Choisissez « reprendre les capteurs » (les
actionneurs gardent leur nom et sont à réappairer) ou « installation vierge ». Dans
ce cas NodOcean peut rester actif avec son ancienne clé.

Les entités de NodOcean sont remplacées par les entités MQTT d'Ocean2MQTT : mettez à
jour vos automatisations et tableaux de bord, puis supprimez l'intégration NodOcean.

## Sauvegarde

**Réglages → Migration et sauvegarde → Télécharger une sauvegarde** : produits,
noms, pièces, réglages et codes Remote Commissioning dans un fichier JSON, à
restaurer au même endroit. Les données de l'add-on sont aussi incluses dans les
sauvegardes de Home Assistant.

## Configuration

- **Clé EnOcean** : choisissez la clé dans la liste.
- **Nom des topics MQTT** : `name` (ocean2mqtt/Salon) ou `id` (ocean2mqtt/0x0512ABCD).
- **Niveau du journal** : `debug` pour voir toutes les trames.
- **Serveur MQTT** : à laisser vide pour utiliser Mosquitto automatiquement. Il se
  modifie aussi dans l'interface (Réglages → Serveur MQTT).
- **Remote Commissioning** : réglages à distance des produits qui le gèrent. Le
  protocole n'est pas chiffré : le code de sécurité d'un produit passe en clair à la
  radio lors d'un déverrouillage (Ocean2MQTT demande confirmation à chaque fois).
  Désactivez l'option si vous n'en avez pas besoin : aucune commande n'est alors
  envoyée.

## Utilisation

Ouvrez **Ocean2MQTT** dans la barre latérale :

- **Ajouter un produit** : choisissez le produit dans la bibliothèque (marque, EEP
  ou référence), lancez l'appairage et suivez la procédure affichée.
- **Mes produits** : commandes, mesures, renommer, supprimer.

Les entités sont créées dans **Paramètres → Appareils et services → MQTT**.

Documentation complète, produits non supportés, dépannage : le
[wiki](https://github.com/eHomeLabs/Ocean2MQTT/wiki).

Les données (configuration et produits appairés) sont dans le dossier privé de
l'add-on et sont incluses dans les sauvegardes Home Assistant.

## Nouveautés de la 0.2.0b14

- **Ajouter un produit par son identifiant EnOcean** (capteurs et interrupteurs),
  sans appuyer sur son bouton d'apprentissage : fiche du produit → « Pas d'accès
  au bouton d'apprentissage ? ».

## Nouveautés de la 0.2.0b13

- **Proposer un nouveau produit EnOcean** : dernière tuile de « Ajouter un
  produit », et lien « Proposer ce produit » pour un émetteur entendu mais inconnu
  (profil et code fabricant préremplis). Catalogue en ligne des produits
  compatibles : https://ehomelabs.github.io/Ocean2MQTT/

## Nouveautés de la 0.2.0b12

- Correction : le bouton « Modifier… » du serveur MQTT n'apparaissait pas dans
  l'add-on.

## Nouveautés de la 0.2.0b11

- **Clé EnOcean HS ou remplacée** : Ocean2MQTT propose d'écrire dans la nouvelle
  clé le Base ID de l'ancienne. Les actionneurs la reconnaissent sans réappairage
  (nombre de changements limité par clé, affiché dans Réglages).
- **Serveur MQTT et topics modifiables** dans Réglages, avec test de la connexion.
  Un réglage fait dans l'interface l'emporte sur le Mosquitto détecté
  automatiquement ; « Revenir au serveur automatique » l'annule.

## Nouveautés de la 0.2.0b10

- Première version publique : l'add-on s'installe depuis le dépôt
  `https://github.com/eHomeLabs/hassio-ocean2mqtt`, image déjà construite (amd64,
  aarch64).
- Photos de tous les produits Ubiwizz de la bibliothèque.

Vous testiez l'add-on **local** ? C'est un autre add-on pour Home Assistant : dans
l'add-on local, **Réglages → Migration et sauvegarde → Télécharger une
sauvegarde**, désinstallez-le, installez celui du dépôt puis importez la sauvegarde
(même écran, « Importer un fichier »).

## Nouveautés de la 0.2.0b9

- Fenêtre de 5 minutes après mise sous tension et session de déverrouillage de
  5 minutes (renouvelée au bout de 4) ; procédure de reset NodOn si le code est perdu.
- Nouveau produit : détecteur de fumée Ubiwizz UBILD001 (F6-05-02) ; photo du
  capteur de qualité d'air UBILD023.

## Nouveautés de la 0.2.0b8

- **Code Remote Commissioning choisi à l'appairage** : automatique (recommandé),
  saisi (QR code ou code au choix) ou aucun. Le code automatique est calculé à
  partir de l'ID du produit et d'un secret propre à l'installation (inclus dans la
  sauvegarde) : toujours le même, impossible à deviner.
- **Détecter le code** d'un produit qui en a déjà un (onglet Remote Commissioning).
- Les codes aléatoires des versions précédentes restent valables.

## Nouveautés de la 0.2.0b7

- Reprise NodOcean : pour un produit générique, choix de la fiche du vrai produit
  (présélectionnée quand une seule correspond).
- **Changer de fiche** (onglet Informations d'un produit) : une autre fiche du même
  profil EEP, sans réappairage ; nom, pièce et topic MQTT conservés.

## Nouveautés de la 0.2.0b6

- Reprise NodOcean : les produits génériques de NodOcean (« EEP-F6-02-01 »…) sont
  repris en produits génériques Ocean2MQTT.

## Nouveautés de la 0.2.0b5

- Option **Remote Commissioning** pour le désactiver complètement.
- Confirmation avant chaque envoi du code de sécurité (déverrouillage), avec
  l'indication de la session en cours (10 min).

## Nouveautés de la 0.2.0b4

- Reprise depuis NodOcean : pour un produit déjà présent dans Ocean2MQTT (réappairé
  avant la reprise), le code Remote Commissioning de NodOcean est repris.

## Nouveautés de la 0.2.0b3

- Reprise des produits de NodOcean for HA (même clé : rien à réappairer), import
  d'un fichier d'export NodOcean, sauvegarde et restauration.
- Changement de clé détecté : les actionneurs à réappairer sont signalés, avec un
  bouton « Réappairer » qui garde leur nom, leur pièce et leurs réglages.

## Nouveautés de la 0.2.0b2

- Puissance et énergie : le rapport automatique des mesures est réglé sur les
  produits avec mesure (au démarrage et après l'appairage), et les actionneurs
  sont interrogés toutes les 60 s, comme dans NodOcean for HA.

## Nouveautés de la 0.2.0b1

- Fiche détaillée de chaque produit (bouton **Détails**) : contrôle, **réglages**
  (LED, bouton local, temporisations, répéteur…), **Remote Commissioning**,
  télégrammes et informations. Les réglages apparaissent aussi dans Home Assistant
  comme entités de configuration.
- **Mode générique** pour un produit absent de la bibliothèque (choix du profil EEP).
- **Suggestion automatique** : quand un produit inconnu envoie sa demande
  d'appairage, Ocean2MQTT propose les fiches qui lui ressemblent ; les capteurs et
  interrupteurs déjà entendus s'ajoutent en un clic.
- Pages **Remote Commissioning** et **Télégrammes** (journal en direct, export CSV).
- Interface en **français et en anglais** (page Réglages).
