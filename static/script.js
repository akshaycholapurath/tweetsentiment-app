document.getElementById("button1").addEventListener("click", function(){
        let value = document.getElementById("uri").value
        const div = document.getElementById("pred")
        fetch('http://127.0.0.1:5000/prediction',{
              method:'post',
              headers:{'Content-Type':'application/json'},
              body:JSON.stringify({
                  text:value
                  })
                })
        .then(res=> res.json())
        .then(data=> div.innerText = `It is a ${data['Prediction']} tweet..`)
        .catch(err=> alert("Please try a different tweet"))
});