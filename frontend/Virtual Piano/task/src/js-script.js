document.addEventListener("keydown", function (event){
   switch (event.key) {
       case "a":
           let sound_a = new Audio("additional/A.mp3");
           sound_a.play();
           break;
       case "s":
           let sound_s = new Audio("additional/S.mp3");
           sound_s.play();
           break;
       case "d":
           let sound_d = new Audio("additional/D.mp3");
           sound_d.play();
           break;
       case "f":
           let sound_f = new Audio("additional/F.mp3");
           sound_f.play();
           break;
       case "g":
           let sound_g = new Audio("additional/G.mp3");
           sound_g.play();
           break;
       case "h":
           let sound_h = new Audio("additional/H.mp3");
           sound_h.play();
           break;
       case "j":
           let sound_j = new Audio("additional/J.mp3");
           sound_j.play();
           break;
       case "w":
           let sound_w = new Audio("additional/W.mp3");
           sound_w.play();
           break;
       case "e":
           let sound_e = new Audio("additional/E.mp3");
           sound_e.play();
           break;
       case "t":
           let sound_t = new Audio("additional/T.mp3");
           sound_t.play();
           break;
       case "y":
           let sound_y = new Audio("additional/Y.mp3");
           sound_y.play();
           break;
       case "u":
           let sound_u = new Audio("additional/U.mp3");
           sound_u.play();
           break;
       default:
           console.log("Warning! Unknown letter is pressed.")
   }
});