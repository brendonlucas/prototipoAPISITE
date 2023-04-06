//(function($) {
//    "use strict";
//
//
//    $(function () {
//        for (var nk = window.location, o = $(".nano-content li a").filter(function () {
//            return this.href == nk;
//        })
//            .addClass("active")
//            .parent()
//            .addClass("active"); ;) {
//            if (!o.is("li")) break;
//            o = o.parent()
//                .addClass("d-block")
//                .parent()
//                .addClass("active");
//        }
//    });
//
//
//    /*
//    ------------------------------------------------
//    Sidebar open close animated humberger icon
//    ------------------------------------------------*/
//
//    $(".hamburger").on('click', function() {
//        $(this).toggleClass("is-active");
//    });
//
//
//
//
//
//    /* TO DO LIST
//    --------------------*/
//    $(".tdl-new").on('keypress', function(e) {
//        var code = (e.keyCode ? e.keyCode : e.which);
//        if (code == 13) {
//            var v = $(this).val();
//            var s = v.replace(/ +?/g, '');
//            if (s == "") {
//                return false;
//            } else {
//                $(".tdl-content ul").append("<li><label><input type='checkbox'><i></i><span>" + v + "</span><a href='#' class='ti-close'></a></label></li>");
//                $(this).val("");
//            }
//        }
//    });
//
//
//    $(".tdl-content a").on("click", function() {
//        var _li = $(this).parent().parent("li");
//        _li.addClass("remove").stop().delay(100).slideUp("fast", function() {
//            _li.remove();
//        });
//        return false;
//    });
//
//    // for dynamically created a tags
//    $(".tdl-content").on('click', "a", function() {
//        var _li = $(this).parent().parent("li");
//        _li.addClass("remove").stop().delay(100).slideUp("fast", function() {
//            _li.remove();
//        });
//        return false;
//    });
//
//
//
//
//
//
//})(jQuery);
//
//
//const body = document.querySelector('body'),
//      sidebar = body.querySelector('nav'),
//      toggle = body.querySelector(".toggle"),
//// searchBtn = body.querySelector(".search-box"),
//      modeSwitch = body.querySelector(".toggle-switch"),
//      modeText = body.querySelector(".mode-text");
//
//
//toggle.addEventListener("click" , () =>{
//    sidebar.classList.toggle("close0");
//})
//
//
//modeSwitch.addEventListener("click" , () =>{
//    body.classList.toggle("dark");
//
//    if(body.classList.contains("dark")){
//        modeText.innerText = "Light mode";
//        localStorage.setItem('theme', "Dark mode");
//    }else{
//        modeText.innerText = "Dark mode";
//        localStorage.setItem('theme', "Light mode");
//    }
//});
//
///*
//searchBtn.addEventListener("click" , () =>{
//    sidebar.classList.remove("close0");
//})
//*/
//
//
//window.onload = function setThemeFunction() {
//    const theme = localStorage.getItem('theme');
//    if (theme == "Light mode"){
//        body.classList.remove("dark");
//    }else{
//        body.classList.toggle("dark");
//    }
//};
//
//
//
