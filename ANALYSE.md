# Analyse de `modele-video.mp4`

## Fiche technique

| | |
|---|---|
| Durée | 15,13 s |
| Format | 1920 × 1078 px (16:9, 2 px plus court que du 1080p standard) |
| Images par seconde | 60 |
| Son | AAC stéréo 48 kHz : un « clic » à 0,50 s, puis une musique rythmée |
| Structure | 8 scènes, puis un **rembobinage accéléré** qui ramène à la toute première image : **la vidéo boucle parfaitement** (image 15,00 s ≈ image 0,00 s) |

## Où trouver les images

- `analyse/images/` : les **61 images** extraites toutes les 0,25 s (`t00.00.png` → `t15.00.png`), en pleine résolution.
- `analyse/planches/` : **6 planches** de 12 images (4 × 3), l'horodatage est inscrit en haut à gauche de chaque vignette.
  - [planche_01](analyse/planches/planche_01.png) : 0,00 → 2,75 s
  - [planche_02](analyse/planches/planche_02.png) : 3,00 → 5,75 s
  - [planche_03](analyse/planches/planche_03.png) : 6,00 → 8,75 s
  - [planche_04](analyse/planches/planche_04.png) : 9,00 → 11,75 s
  - [planche_05](analyse/planches/planche_05.png) : 12,00 → 14,75 s
  - [planche_06](analyse/planches/planche_06.png) : 15,00 s
- `analyse/zooms/` : **14 planches « au ralenti »** (une image toutes les 0,083 s, soit 12 images/s) sur chaque transition, pour voir le détail des mouvements.

---

## 1. Les couleurs exactes

Ces valeurs ont été mesurées au pixel sur les images. La compression vidéo fait varier chaque teinte de ±2 sur chaque canal ; la valeur indiquée est la plus fréquente.

| Rôle | Hex | Aperçu de l'usage |
|---|---|---|
| **Fond crème** (scènes claires) | `#EDE9E1` (varie entre `#EBEAE3` et `#EEE8E3`) | Fond des scènes 1, 2, 3 (graphique), losange/pilule, trame de points |
| **Noir chaud** (fond sombre et texte) | `#131313` / `#141210` | Texte « Reduce Motion », « Motion », fonds des scènes sombres, losange noir |
| **Orange signature** | `#FE4D1C` (≈ `#FF4D1C`) | Interrupteur allumé, point du « i », balle, cercle, fond orange plein, « 0 », point final de « designer. » |
| **Crème clair (texte sur noir)** | `#EBEAE3` | « Motion designer. », « keyframes », lettres de l'anneau 3D au premier plan |
| **Gris moyen** (sous-titre) | `#999996` | « Opus 5.5 » |
| **Gris foncé** (profondeur 3D) | `#505050` | Lettres de l'anneau qui passent **à l'arrière** (vues à l'envers) |
| **Beige grisé** (interrupteur éteint) | `#CFC5B9` | Rail de l'interrupteur en position OFF |
| **Blanc pur** | `#FFFFFF` | Bouton rond de l'interrupteur |
| **Gris pointillé** | `#95918B` (`#68645E` au cœur du trait) | Ligne cible en pointillés du graphique |
| **Contours fantômes** | orange `#FE4D1C` ou noir, opacité ~30–40 % | Le contour de la forme précédente reste visible puis s'efface (ex. contour de pilule `#692B20` sur fond noir, c'est l'orange à ~35 %) |

**Règle de palette :** seulement **3 couleurs** : crème, noir et orange. Le fond change d'une scène à l'autre (crème → noir → orange → crème → noir), et la couleur de la forme s'inverse en même temps. L'orange est toujours la couleur « héroïne » (le point qui voyage à travers toute la vidéo).

---

## 2. La typographie

On ne peut pas identifier une police avec certitude à partir de pixels. Voici ce qu'on observe, avec les polices gratuites les plus proches.

| Texte | Style observé | Taille approx. (sur 1080 px de haut) | Police proche (Google Fonts) |
|---|---|---|---|
| « Reduce Motion » | Sans-serif grotesque, **Bold/ExtraBold**, interlettrage serré, R majuscule, reste en minuscules | hauteur de capitale ≈ 120 px | *Inter Tight* ExtraBold, *Bricolage Grotesque* Bold |
| « Motion » (géant, centré) | Même famille en **Black (900)**, très serré (≈ −3 %) | hauteur de capitale ≈ 290 px | *Inter Tight* Black |
| « EASING · KINETIC TYPE · 3D · SOUND · LOOPS · SPRINGS · » | **MAJUSCULES**, Bold, légèrement condensé, séparateurs « · » (point médian) | ≈ 70–90 px selon la perspective | *Inter Tight* Bold / *Archivo* ExtraBold |
| « Opus 5.5 » | Regular/Medium, gris `#999996` | ≈ 60 px de capitale | *Inter* Medium |
| « Motion designer. » | Bold/ExtraBold, crème, point final **orange** | ≈ 160 px de capitale | *Bricolage Grotesque* ExtraBold : le « g » et le « y » en sont très proches |
| « 0 keyframes » | Même style ; le **« 0 » en orange**, le reste en crème. Le « y » a une queue droite caractéristique | ≈ 150 px | *Bricolage Grotesque* ExtraBold |

**Mise en page du titre final :** bloc **aligné à gauche**, marge gauche ≈ 150 px, interlignage très serré (les lignes se touchent presque). Le « i » de « Motion » est **sans point** (« ı ») : son point est un rond orange séparé qui peut s'envoler.

---

## 3. Déroulé scène par scène (et comment chaque texte apparaît)

> Repères : *planche* = vignettes toutes les 0,25 s ; *zoom* = planches au ralenti dans `analyse/zooms/`.

### Scène 1 : l'interrupteur (0,00 → 1,05 s) · zoom `01_interrupteur`
- **0,00–0,50 :** gros plan très serré sur un interrupteur iOS **allumé** (orange). Le curseur de souris noir est posé sur le bouton blanc. On ne voit que le « n » de « Motion » à gauche.
- **0,50 :** **clic** (on entend le son). Le bouton glisse vers la gauche et le rail passe de l'orange au beige `#CFC5B9` en ≈ 0,3 s.
- **0,53–0,85 :** **dézoom très rapide** avec **flou de mouvement horizontal** : la caméra recule et révèle le libellé « **Reduce Motion** ». L'effet est rapide au départ et ralentit doucement à la fin (*ease-out*).
- **0,85–1,05 :** pause courte, tout est net.
- **Apparition du texte :** il n'y a pas d'animation propre au texte. Il apparaît par **le mouvement de caméra** (le dézoom flouté).

### Scène 2 : les lettres tombent (1,05 → 1,75 s) · zoom `02_lettres_tombent`
- **Effet « lettre par lettre » :** les lettres de « **Reduce** » se décrochent **une par une, en commençant par le R**. Chaque lettre **pivote** et **tombe** en bas à gauche comme sous l'effet de la gravité, avec un décalage d'environ 0,03 s entre deux lettres. Le mot se courbe en arc, comme une chaîne qui tombe.
- L'interrupteur **tombe aussi**, en bas à droite.
- **C'est le clin d'œil de la vidéo :** on active « Réduire les animations »… et c'est l'inverse qui se produit.
- « **Motion** » reste seul, glisse au centre et **grossit** (*scale* ≈ ×1,8) jusqu'à 1,75 s.

### Scène 3 : « Motion » et la balle (1,75 → 3,40 s) · planche 01-02
- « Motion » est énorme et centré, avec un léger zoom avant continu (*push-in* lent).
- **≈ 2,40 :** le **point du « i » (orange) saute** hors de la lettre, qui devient « Motıon ».
- **2,50–3,35 :** le point **rebondit comme une balle** : il s'**étire** quand il va vite (ellipse, *squash & stretch*) et laisse une **traînée floue rose-orange** derrière lui. On compte 2 rebonds.

### Transition 3 → 4 : panoramique filé (3,40 → 3,55 s) · zoom `03_motion_vers_graph`
- **Panoramique filé** (*whip pan*) : tout part vers la gauche avec un **flou de mouvement horizontal très fort** (3,417 s), puis les axes d'un graphique arrivent par la droite.
- La balle orange garde sa trajectoire et **tombe pile sur l'origine** du graphique (3,75–3,83 s). C'est le même objet d'une scène à l'autre : un *match cut*.

### Scène 4 : le graphique « ressort » (3,55 → 5,05 s) · planche 02
- Graphique minimaliste : 2 axes noirs fins (≈ 2 px) et une **ligne cible en pointillés** gris.
- **3,85–5,00 :** la balle **dessine une courbe de ressort** (*spring*). Elle monte vite, **dépasse** la cible, redescend sous la ligne, puis se stabilise après 2 petites oscillations amorties. La courbe est tracée **derrière** la balle, avec de petits points réguliers dessus (les « échantillons » de l'animation).
- **4,25 :** l'étiquette « **+22 %** » (Bold noir), reliée au pic par un petit trait, apparaît avec un **flou qui se met au point** (*blur-in*, ≈ 0,15 s). C'est le dépassement du ressort (*overshoot*).

### Transition 4 → 5 : plongée dans la courbe (5,05 → 5,65 s) · zoom `04_graph_vers_cercle`
- **5,05 :** le graphique **bascule en 3D** (perspective) avec du flou.
- **5,13–5,60 :** **zoom extrême** sur la fin de la courbe. Le trait devient une grosse ligne noire avec des perles, et la balle devient un **grand disque orange** qui glisse vers le centre.

### Scène 5 : la métamorphose des formes, une coupe par temps (5,65 → 7,50 s) · zooms `04`, `05`, `06`
Chaque **coupe franche** tombe exactement sur un temps de la musique (toutes les **0,47 s**). À chaque coupe, **fond et forme échangent leurs couleurs** :

| Temps | Fond | Forme | Mouvement |
|---|---|---|---|
| **5,65** | noir `#141210` | disque orange (≈ 520 px de diamètre) | coupe nette, forme immobile |
| **6,12** | **orange** | **noir** | le cercle **se transforme en carré arrondi posé sur la pointe (losange)** en **tournant** ; le contour fin du cercle reste visible et s'efface (≈ 0,4 s) |
| **6,58** | crème | losange **orange** | le losange **s'étire en pilule** horizontale en tournant (flou de mouvement) ; le contour du losange reste en fantôme orange qui s'efface |
| **7,05** | noir | pilule orange | la pilule **rétrécit** à l'intérieur de son propre contour jusqu'à devenir un **petit point orange** (≈ 50 px) ; le contour s'efface vers 7,50 |

### Scène 6 : l'anneau de texte en 3D (7,55 → 9,40 s) · zoom `07_anneau`, planches 03-04
- Le texte « **EASING · KINETIC TYPE · 3D · SOUND · LOOPS · SPRINGS ·** » forme un **anneau en 3D** qui **tourne autour du point orange**, vu en plongée.
- **Apparition (7,55–7,90) :** l'anneau **jaillit du point** en s'agrandissant très vite, avec un fort **flou de mouvement**, puis se met au point.
- **Profondeur :** les lettres de devant sont crème `#EBEAE3`, grandes et nettes. Celles de derrière sont gris `#505050`, plus petites et **vues à l'envers** (en miroir).
- **Rotation :** régulière, ≈ 1/8 de tour par 0,5 s.
- **9,25–9,40 :** le point orange **tombe** hors de l'anneau, vers le bas.

### Scène 7 : la trame de points et l'onde de choc (9,42 → 11,30 s) · zooms `08`, `09`
- **9,42 :** **coupe** sur un fond crème couvert d'une **grille régulière de petits points noirs** (trame). Un **grand disque orange** avec une **ombre grise** décalée en bas à droite **rétrécit** jusqu'à 9,85 s : il « atterrit » sur la surface, et l'ombre rejoint le point.
- **10,00–10,50 :** au moment de l'impact, les points de la grille **gonflent en anneaux concentriques** qui s'éloignent du centre : une **onde de choc** (*ripple*) qui se répète 2–3 fois.
- **10,50–10,90 :** les points du centre grossissent jusqu'à **se toucher et devenir un aplat noir** qui envahit tout l'écran en ≈ 0,35 s (effet de trame d'imprimerie qui noircit).
- **10,90–11,30 :** noir avec le petit point orange au centre (pause).

### Scène 8 : le titre final (11,30 → 13,55 s) · zooms `10_titre`, `11_keyframes`, `12_sortie_titre`
- **11,30–11,80 :** le point orange **s'envole en haut à droite** (étiré par la vitesse).
- **Apparition des textes :** **révélation par masque, du bas vers le haut** (*mask reveal / slide-up*). Chaque ligne monte depuis une ligne invisible qui la coupe : on voit d'abord le haut des lettres, puis le mot entier. Le **décalage** entre lignes est d'environ 0,08 s :
  - « Opus 5.5 » commence à 11,38 s ;
  - « Motion designer » commence à 11,47 s et se termine vers 11,65 s.
- **11,80 :** le point orange **atterrit à la fin de « designer »** et **devient le point final** « . » (petit écrasement à l'impact).
- **12,30–12,50 :** « **0 keyframes** » apparaît par le même **masque montant**. En même temps, tout le bloc **remonte légèrement** pour rester centré.
- **12,50–13,30 :** pause, lecture du message.
- **Sortie (13,35–13,55) :** inverse de l'entrée : « 0 keyframes » **redescend derrière son masque**, puis « Motion designer » se **floute** et disparaît. Il ne reste que le point orange.

### Final : le rembobinage (13,60 → 15,13 s) · zooms `13_rembobinage`, `14_fin`
- Toute la vidéo est **rejouée à l'envers en accéléré** (≈ ×8), avec beaucoup de flou de mouvement. Chaque scène ne dure que 1 à 5 images : trame (13,67) → anneau 3D (13,83–13,95) → pilule sur fond gris (14,02, deux scènes fondues l'une dans l'autre) → losange sur orange (14,10) → courbe (14,18) → graphique (14,27) → axes (14,35) → « Motion » (14,43).
- **14,45–15,00 :** à vitesse un peu plus lente, l'intro à l'envers : le point revient sur le « i », les lettres de « Reduce » **remontent** à leur place, la caméra **zoome** sur l'interrupteur, qui **se rallume en orange**. Le curseur sort par le bas à droite.
- **La dernière image est identique à la première** : la vidéo peut tourner en boucle sans raccord visible.

---

## 4. Les transitions entre scènes (récapitulatif)

| # | Moment | Type de transition |
|---|---|---|
| 1 | 0,53 s | **Dézoom caméra rapide + flou de mouvement** |
| 2 | 1,05 s | **Physique** : les lettres tombent, le mot restant se recentre et grossit |
| 3 | 3,40 s | **Panoramique filé** (*whip pan*) avec gros flou horizontal + la balle passe d'une scène à l'autre (*match cut*) |
| 4 | 5,05 s | **Bascule 3D + zoom extrême** dans la courbe |
| 5 | 5,65 / 6,12 / 6,58 / 7,05 s | **Coupes franches sur le temps**, avec **inversion des couleurs** fond/forme + **morphing** de forme (cercle → losange → pilule → point) et contour fantôme de la forme précédente |
| 6 | 7,55 s | L'anneau **jaillit du point** (zoom + flou) |
| 7 | 9,42 s | **Coupe franche** pendant que la balle tombe (*match cut* sur le point) |
| 8 | 10,50 s | **Trame qui noircit** : les points grossissent jusqu'au noir plein |
| 9 | 13,55 s | **Sortie par masque** (inverse de l'entrée) |
| 10 | 13,60 s | **Rembobinage accéléré** jusqu'au début → **boucle** |

**Fil conducteur :** le **point orange** est présent dans toutes les scènes (point du « i » → balle → curseur du graphique → disque → losange → pilule → centre de l'anneau → impact sur la trame → point final de « designer. »). C'est lui qui fait le lien d'une scène à l'autre.

---

## 5. Le rythme

- **Tempo de la musique :** ≈ **128 BPM**, soit **un temps toutes les 0,47 s** (mesuré sur la piste audio).
- **Son :** un **clic** sec à 0,50 s (le clic sur l'interrupteur), puis la musique démarre vers 1,0 s et monte à pleine puissance vers 1,75 s. Pendant le rembobinage (après 13,5 s), le volume baisse (de −13 dB à −41 dB) jusqu'à la fin.
- **Coupes calées sur le temps :** 5,65 → 6,12 → 6,58 → 7,05 s, **exactement 0,47 s d'écart**. Les coupes suivantes (9,42 s, puis le noir vers 10,85 s) tombent aussi sur la grille des temps.
- **Durée des scènes :**

| Scène | Durée |
|---|---|
| 1. Interrupteur | 1,05 s |
| 2. Lettres qui tombent | 0,70 s |
| 3. « Motion » + balle | 1,65 s |
| 4. Graphique ressort | 1,50 s |
| (plongée dans la courbe) | 0,60 s |
| 5. Formes (4 × 1 temps) | 1,90 s |
| 6. Anneau 3D | 1,85 s |
| 7. Trame + onde | 1,90 s |
| 8. Titre final | 2,25 s |
| Rembobinage | 1,50 s |

- **Alternance tension / repos :** rapide (dézoom), lent (« Motion »), rapide (whip), lent (ressort), **très rapide** (une forme par temps), lent (anneau), moyen (onde), **lent** (titre, pour laisser lire), **très rapide** (rembobinage).
- **Les courbes de vitesse (*easing*) :**
  - quasiment tout utilise un **départ très rapide puis un ralenti long** (*ease-out* exponentiel, type `expo.out` / `power4.out`) ;
  - les rebonds et la courbe utilisent un **ressort** avec dépassement (*spring/back.out*, dépassement ≈ 22 %) ;
  - le **flou de mouvement** est présent sur chaque déplacement rapide : c'est ce qui rend la vidéo si fluide ;
  - **aucun fondu enchaîné classique**, sauf pendant le rembobinage : tout passe par le mouvement, le morphing ou des coupes nettes.

---

## 6. Aide-mémoire pour refaire ce style avec HyperFrames

```css
:root {
  --creme:   #EDE9E1;
  --noir:    #131313;
  --orange:  #FE4D1C;
  --texte-clair: #EBEAE3;
  --gris:    #999996;
  --gris-3d: #505050;
  --rail-off:#CFC5B9;
}
```

- Format 1920×1080, 60 i/s, musique ≈ 128 BPM (temps = 0,469 s).
- 3 couleurs seulement, et on inverse fond/forme à chaque coupe.
- Un seul objet orange qui voyage d'une scène à l'autre.
- Textes : sans-serif grotesque très gras et serré ; entrées par **masque montant** décalé de ≈ 0,08 s par ligne ; mouvements en `expo.out` avec flou de mouvement.
- Finir par un rembobinage rapide vers la première image pour une boucle parfaite.
