function typewriter(){
    const text="I'm FINN-AI"
    let index=0
    while(index<=text.length){
        document.getElementById("typewriter").innerHTML+=text.charAt(index)
        index++
        setTimeout(typewriter,100)
    }
}
typewriter()