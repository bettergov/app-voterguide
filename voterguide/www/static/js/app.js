let appInit = function() {
    let filters = document.getElementsByClassName('candidate-filter');

    const params = new URLSearchParams(location.search);

    for (var i = 0; i < filters.length; i++) {
        let f = filters[i];
        f.addEventListener('click', function() {
            console.log(f);
            var key = f.dataset.candidateKey;
            let candidates = new Set();
            for (let v of params.values()) candidates.add(v);

            if (candidates.has(key)) {
                candidates.delete(key);
            } else {
                candidates.add(key);
            }

            params.delete('candidate[]');
            for (let c of candidates) {
                params.append('candidate[]', c);
            }
            
            window.history.replaceState({}, '', `${location.pathname}?${params}`);
            window.location.reload();
        }, false);
    };


    let responses = document.getElementsByClassName('response__text');
    for (var i = 0; i < responses.length; i++) {
        let r = responses[i];
        if (r.clientHeight > 150) r.parentNode.classList.add("collapsed");
    }

    let expanders = document.getElementsByClassName('response-expand');
    for (var i = 0; i < expanders.length; i++) {
        let e = expanders[i];
        e.addEventListener('click', function() {
            e.parentNode.classList.remove("collapsed");
        }, false);
    }
}

document.addEventListener("DOMContentLoaded", function(event) { 
    appInit();
});