let appInit = function() {
    let filters = document.getElementsByClassName('candidate-filter');

    const params = new URLSearchParams(location.search);

    for (let f of filters) {
        f.addEventListener('click', function() {
            let key = f.dataset.candidateKey;
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
    }


    for (let r of document.getElementsByClassName('response__text')) {
        if (r.clientHeight > 150) r.parentNode.classList.add("collapsed");
    }

    for (let e of document.getElementsByClassName('response-expand')) {
        e.addEventListener('click', function() {
            e.parentNode.classList.remove("collapsed");
        }, false);
    }
}

document.addEventListener("DOMContentLoaded", function(event) { 
    appInit();
});