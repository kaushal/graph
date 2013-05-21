
function parseJson(){
    var url = "http://www.contextminer.org/api.php/campaigns?u=chirags%40rutgers.edu&cid=516&source=youtube&everytime=1&ytid=wm4o1fYtCTQ&page=4&limit=25&fmt=json"
   $.getJSON(url, function(data) {
         alert(data.name);
   });
}
