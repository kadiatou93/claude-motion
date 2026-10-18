---
workflow: general-video
flow: companion
storyboard: yes
message: "Jokko, le bon prestataire, au bon prix, près de chez toi."
aspect: "16:9"
size: "1920x1080"
fps: 60
language: fr
length: "40.5s (durée de la voix + 1 s de signature)"
---

## Intent
Vidéo promo JOKKO calée mot par mot sur la voix off ElevenLabs (assets/voix.mp3), dans le style de ANALYSE.md :
3 couleurs (orange #FE4D1C, blanc cassé #EDE9E1, noir #131313), point orange fil conducteur, typographie
Instrument Serif (comme la planche de marque Jokko) + Bricolage Grotesque.

## Customizations (règles imposées)
1. Gros textes lettre par lettre : chaque lettre monte en s'étirant, flou vertical, 2 images de décalage.
2. Tout ce qui bouge laisse des échos (3 copies fantômes transparentes, en retard de 0,035 s chacune).
3. Certains mots sortent d'une fente, derrière une ligne horizontale.
4. Aucune coupe sèche : la scène sortante part en traînée floue, la suivante arrive dans la même direction avec un bord dégradé.
5. Le texte vit toujours : zoom continu (×1,06 par scène) et lettres qui frémissent.
Images de contrôle avant le rendu final.

## Notes
Calage mot par mot provisoire : calculé à partir des silences de la voix (huggingface.co bloqué, pas de modèle de
reconnaissance vocale). Les temps sont dans le tableau `W` de index.html et dans assets/words.json.
