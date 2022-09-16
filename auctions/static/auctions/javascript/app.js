function maxCategorieChecked(name, obj, max) {
  var count = 0;
  var checkboxes = document.getElementsByName(name);
  for (var i = 0; i < checkboxes.length; i++) {
    if (checkboxes[i].checked) {
      count++;
    }
  }
  if (count > max) {
    $("#alert-modal").modal("show");
    obj.checked = false;
  }
}

// random cover
var images = [
  "https://images.unsplash.com/photo-1579547621113-e4bb2a19bdd6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2139&q=80",
  "https://images.unsplash.com/photo-1548081087-a8a3bc4ff088?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1974&q=80",
  "https://images.unsplash.com/photo-1503454537195-1dcabb73ffb9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1972&q=80",
  "https://images.unsplash.com/photo-1605013939843-ec5f3a726ff1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2008&q=80",
  "https://images.unsplash.com/photo-1620566160396-c1064289b0e6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1935&q=80",
  "https://images.unsplash.com/photo-1622189431943-f849d606f31c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2127&q=80",
  "https://images.unsplash.com/photo-1605888705092-f3b4b8f45495?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1974&q=80",
  "https://images.unsplash.com/photo-1611844088399-dfac5dc474a4?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1974&q=80",
  "https://images.unsplash.com/photo-1537204319452-fdbd29e2ccc7?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1974&q=80",
  "https://images.unsplash.com/photo-1563223566-f731efbdbab0?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1935&q=80",
  "https://images.unsplash.com/photo-1560507041-ea7882a63ca1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1974&q=80",
  "https://images.unsplash.com/photo-1600470902715-816eb7817285?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1974&q=80",
  "https://images.unsplash.com/photo-1602092301958-cd6ad92b6c1d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1974&q=80",
];

var randomNumbers = [];
while (randomNumbers.length < images.length) {
  var r = Math.floor(Math.random() * images.length);
  if (randomNumbers.indexOf(r) === -1) randomNumbers.push(r);
}
console.log(randomNumbers);

window.onload = function () {
  var image = document.getElementById("cover-image");
  image.setAttribute("src", images[randomNumbers[0]]);

  for (var i = 0; i < randomNumbers.length; i++) {
    var newDiv = document.createElement("div");
    newDiv.setAttribute("class", "carousel-item");
    newDiv.setAttribute("data-interval", "5000");
    var newImg = document.createElement("img");
    newImg.setAttribute("src", images[randomNumbers[i]]);
    newImg.setAttribute("class", "d-block w-100");
    newDiv.appendChild(newImg);
    var currentDiv = document.getElementById("carousel");
    currentDiv.appendChild(newDiv);
  }
};
