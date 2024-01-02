// ==UserScript==
// @name         Stopwatch for Bunpro
// @namespace    http://tampermonkey.net/
// @version      2024-01-02
// @description  try to take over the world!
// @author       You
// @match        http://*/*
// @icon         data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Your code here...
    alert("hello");

    // must wait for all elements to render first

    // insert the element

    // calculate the stopwatch timer

    ultTag = document.getElementsByClassName("flex items-center gap-4 md:gap-12");

    p = ultTag[0];

    console.log(p);

    btn = document.createElement("button");
    btn.innerHTML = "Copy";
    btn.onClick = () => {
        alert("this button works");
    }

    p.insertBefore(btn, p.childNodes[0]);
})();