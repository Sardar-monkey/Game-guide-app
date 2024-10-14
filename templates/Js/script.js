function ShowMenu() {
    let menu = document.getElementById("overlay"); 
    if (menu.style.display === "none") {
        menu.style.display = "block";
    } else {
        menu.style.display = "none";
    }
}

function ShowDelete() {
    let delet = document.getElementById("overlay2"); 
    if (delet.style.display === "none") {
        delet.style.display = "flex";
    } else {
        delet.style.display = "none";
    }
}