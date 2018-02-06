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
}

document.addEventListener("DOMContentLoaded", function(event) { 
    appInit();
});