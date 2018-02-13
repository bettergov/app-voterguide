function appInit() {
    "use strict";
    var filters = document.getElementsByClassName('candidate-filter');

    var params = new URLSearchParams(location.search);

    for (var i = 0; i < filters.length; i++) {
        var filter = filters[i];
        filter.addEventListener('click', function() {
            var key = this.dataset.candidateKey;

            // Get candidates from URL
            var candidates = new Set(params.getAll('candidate[]'));

            if (candidates.has(key)) {
                candidates.delete(key);
            } else {
                candidates.add(key);
            }

            params.delete('candidate[]');
            candidates.forEach(function(c){ params.append('candidate[]', c); })

            window.history.replaceState({}, '', `${location.pathname}?${params}`);
            window.location.reload();
        }, false);
    };


    var responses = document.getElementsByClassName('response__text');
    for (var i = 0; i < responses.length; i++) {
        var r = responses[i];
        if (r.clientHeight > 150) r.parentNode.classList.add("collapsed");
    }

    var expanders = document.getElementsByClassName('response-expand');
    for (var i = 0; i < expanders.length; i++) {
        var e = expanders[i];
        e.addEventListener('click', function() {
            e.parentNode.classList.remove("collapsed");
        }, false);
    }
}

document.addEventListener("DOMContentLoaded", function(event) { 
    appInit();
});