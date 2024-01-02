// ==UserScript==
// @name         Stopwatch for Bunpro
// @namespace    http://tampermonkey.net/
// @version      0.0.1
// @description  Starts a stopwatch upon starting Bunpro Reviews.
// @author       PowerAWBS
// @match        https://bunpro.jp/reviews*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Your code here...
    alert("hello");

    function addTimer() {
        btn = document.createElement("button");
        btn.innerHTML = "Copy";
        btn.onClick = () => {
            alert("this button works");
        }

        p.insertBefore(btn, p.childNodes[0]);

    }

    ultTag = document.getElementsByClassName("flex items-center gap-4 md:gap-12");

    p = ultTag[0];

    console.log(p);

})();

// https://www.youtube.com/watch?v=U4dSWJFIQ0A