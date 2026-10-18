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

## Audio
- Un bruitage par mot qui apparaît : 6 tics et 6 petits souffles synthétisés, jamais le même deux fois de suite
  (souffle pour les mots qui sortent d'une fente, tic pour les mots lettre par lettre). Liste : assets/audio/bruitages.txt.
- Coups de basse sur les moments forts : Jokko, 70, 20, Plombier, Électricien, Femme de ménage, vérifiés, FCFA, Dakar, Jokko, Jokko.
- Bruitages + basses réglés à 7 dB sous la voix (mesuré : voix -28,1 LUFS, bruitages -35,1 LUFS).
- Musique originale 122 BPM (synthétisée, libre de droits), 4 dB sous la voix hors parole, baisse de 12 dB quand la voix parle.
- Mix final masterisé à -14 LUFS intégré, pic vrai ≤ -1 dBTP (Instagram). Script : assets/audio/build_audio.py.
