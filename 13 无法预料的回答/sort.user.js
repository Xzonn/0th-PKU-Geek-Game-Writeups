// ==UserScript==
// @name         13 无法预料的问答
// @namespace    https://xzonn.top/
// @version      0.9
// @description  Now, it's up to you to do the next one.
// @author       Xzonn
// @match        http://prob11.geekgame.pku.edu.cn/*
// @icon         http://pku.edu.cn/favicon.ico
// @require      https://code.jquery.com/jquery-3.6.0.min.js
// @grant        none
// ==/UserScript==

/* global $ */
(function () {
    let choices = $(".radio input[type='radio']");
    let lastEmoji = localStorage.lastEmoji.split("|");
    let lastSelectedEmoji = localStorage.lastSelectedEmoji;
    let emojiSort = JSON.parse(localStorage.emojiSort || "[]");
    let emojiSortBefore = emojiSort.join("");
    let lastResult;
    let results = JSON.parse(localStorage.results || "[]");
    for (let i = 0; i < lastEmoji.length; i++) {
        if ((lastEmoji[i] != lastSelectedEmoji) && (emojiSort.indexOf(lastEmoji[i]) == -1)) {
            emojiSort.splice(0, 0, lastEmoji[i]);
        }
    }
    let otherMaxPos = Math.max(...lastEmoji.filter(x=>x!=lastSelectedEmoji).map(x=>emojiSort.indexOf(x)));
    let selectedPos = emojiSort.indexOf(lastSelectedEmoji);
    if ($(".alert").text().toLowerCase().indexOf("this is bad") > -1) {
        // 上一个选择的 Emoji 不是最大的
        lastResult = false;
        if (selectedPos > otherMaxPos) {
            if (selectedPos > -1) {
                emojiSort.splice(selectedPos, 1);
            }
            emojiSort.splice(otherMaxPos, 0, lastSelectedEmoji);
        }
        if (emojiSort.indexOf(lastSelectedEmoji) == -1) {
            emojiSort.splice(0, 0, lastSelectedEmoji);
        }
        let emojiSortAfter = emojiSort.join("");
        if (emojiSortBefore == emojiSortAfter) {
            throw '咋回事';
        }
    } else if ($(".alert").text().toLowerCase().indexOf("回答正确") > -1) {
        // 上一个选择的 Emoji 是最大的
        lastResult = true;
        if (selectedPos < otherMaxPos) {
            if (selectedPos > -1) {
                emojiSort.splice(selectedPos, 1);
            }
            emojiSort.splice(otherMaxPos + 1, 0, lastSelectedEmoji);
        }
    }
    results.push(lastEmoji.join("") + "|" + lastSelectedEmoji + "|" + (+lastResult));
    localStorage.results = JSON.stringify(results);
    localStorage.emojiSort = JSON.stringify(emojiSort);
    console.log(emojiSort.join(""));

    let sorted = choices.toArray().map(x=>[x, emojiSort.indexOf(x.value)]).sort((x,y)=>(y[1] - x[1]));
    sorted[0][0].checked = true;

    $("form").on("submit", function () {
        localStorage.lastEmoji = choices.toArray().map(x=>x.value).join("|");
        localStorage.lastSelectedEmoji = choices.toArray().filter(x=>x.checked)[0].value;
    });

    setTimeout(function () {
        $("form").submit();
    }, 1000);
})();