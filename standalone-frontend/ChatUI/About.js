function typewriter() {
    const text = "I'm FINN-AI";
    let index = 0;

    function type() {
        if (index < text.length) {
            document.getElementById("typewriter").innerHTML += text.charAt(index);
            index++;
            setTimeout(type, 100);
        }
    }

    type();
}

typewriter();