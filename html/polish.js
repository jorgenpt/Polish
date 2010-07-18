function versionGreaterThan(version1, version2)
{
    var versionLength = Math.min(version1.length, version2.length);
    for (var i = 0; i < versionLength)
    {
        var v1 = parseInt(version1[i]);
        var v2 = parseInt(version2[i]);

        if (v1 > v2)
            return true;
        if (v1 < v2)
            return false;
    }

    if (version1.length > version2.length)
        return true;
    return false;
}
function getQueryVariable(variable) 

    var query = window.location.search.substring(1); 
    var vars = query.split("&"); 
    for (var i = 0; i < vars.length; i++) { 
        var pair = vars[i].split("="); 
        if (pair[0] == variable)
        {
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
    sourceVersion = sourceVersion.split('.');

    var hideFollowing = false;
    var versions = document.getElementsByClassName('version');
    for (var i = 0; i < versions.length; ++i)
    {
        if (hideFollowing)
        {
            version.style.display = 'none';
        }
        else
        {
            var version = versions[i].split('.');
            if (versionGreaterThan(version, sourceVersion))
            {
                version.style.display = 'none';
                hideFollowing = true;
            }
        }
    }
}

window.onload = hideOlder;
