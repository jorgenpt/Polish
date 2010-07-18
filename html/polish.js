function getQueryVariable(variable) { 
    var query = window.location.search.substring(1); 
    var vars = query.split("&"); 
    for (var i=0;i<vars.length;i++) { 
        var pair = vars[i].split("="); 
        if (pair[0] == variable) { 
            return pair[1]; 
        } 
    } 
    return null;
} 

function hideOlder()
{
    var sourceVersion = getQueryVariable('version');
    if (!sourceVersion)
        return;

    var hideFollowing = false;
    var versions = document.getElementsByClassName('version');
    for (var i = 0; i < versions.length; ++i)
    {
        var version = versions[i];
        if (version.id == sourceVersion)
            hideFollowing = true;

        if (hideFollowing)
            version.style.display = 'none';
    }
}

window.onload = hideOlder;
