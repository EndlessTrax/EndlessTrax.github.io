/*
    My Custom JavaScript
*/

$(document).ready(function(){

    // Gets the Navigation bar height to offset later
    var navHeight = $('nav').outerHeight()

    // On Click function
    $('#down-arrow').click(function(e){
        
        // Turns the href into an JS Object to use with JQuery. 
        // If the variable is not an object, it won't work!
        var linkHref = $(this).attr('href');

        // Main Animation function
        // 1000 = 1000ms - i.e. time to scroll down
        $('html, body').animate({
            scrollTop: $(linkHref).offset().top - navHeight
        }, 1000);       
        
        // Disables the default scroll
        e.preventDefault();
    });
});
