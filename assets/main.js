//
// JavaScript File for Ricky White .dev
//

const realPythonJsonPath = "json_data/real_python_tuts.json";
const realPythonArticleDiv = document.getElementById("real-python-articles");

$.getJSON(realPythonJsonPath, function(data) {
  data.forEach(element => {
    let item = document.createElement("li");
    item.innerHTML = '<a href="' + element.link + '">' + element.title + "</a>";
    realPythonArticleDiv.appendChild(item);
  });
});
