document.addEventListener("keydown", function (event){
   switch (event.key) {
       case "a":
           console.log("The 'a' key is pressed.");
           break;
       case "s":
           console.log("The 's' key is pressed.");
           break;
       case "d":
           console.log("The 'd' key is pressed.");
           break;
       case "f":
           console.log("The 'f' key is pressed.");
           break;
       case "g":
           console.log("The 'g' key is pressed.");
           break;
       case "h":
           console.log("The 'h' key is pressed.");
           break;
       case "j":
           console.log("The 'j' key is pressed.");
           break;
       default:
           console.log("Warning! Unknown letter is pressed.")
   }
});