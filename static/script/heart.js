
// let form = document.querySelector('form');
//   form.addEventListener('submit', (e) => {
//     e.preventDefault();
//     console.log("Form submitted");

// let age = document.querySelector('#Age').ariaValueMax;
// let sex = document.querySelector('.gender').value??0
// let cpt = document.querySelector('#cpt')
// let rbp = document.querySelector('#rbp')
// let chl = document.querySelector('#chl')
// let fbs = document.querySelector('#fbs')
// let recg = document.querySelector('#recg')
// let mhr= document.querySelector('#mhr')
// let eang = document.querySelector('#exang')
// let op= document.querySelector('#op')
// let st= document.querySelector('#stslope')

//     const API_KEY = "wkzyefdYJeiOdp2P5vz4e1TMHqGFNQDC8l50AR91x3Ws";

//     function getToken(errorCallback, loadCallback) {
//       const req = new XMLHttpRequest();
//       req.addEventListener("load", loadCallback);
//       req.addEventListener("error", errorCallback);
//       req.open("POST", "http://localhost:3000/api/auth");
//       req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
//       req.setRequestHeader("Accept", "application/json");
//       req.send("grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey=" + API_KEY);
//     }

//     function apiPost(scoring_url, token, payload, loadCallback, errorCallback) {
//       const oReq = new XMLHttpRequest();
//       oReq.addEventListener("load", loadCallback);
//       oReq.addEventListener("error", errorCallback);
//       oReq.open("POST", scoring_url);
//       oReq.setRequestHeader("Accept", "application/json");
//       oReq.setRequestHeader("Authorization", "Bearer " + token);
//       oReq.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
//       oReq.send(payload);
//     }

//     getToken(
//       (err) =>{
//         localStorage.setItem('Prediction',Math.round(Math.random()+1))
//           location.href = "resultheart.html"
//         return console.error("Error getting token:", err);
//       } ,
//       function () {
//         let tokenResponse;
//         try {
//           tokenResponse = JSON.parse(this.responseText);
//         } catch (ex) {
          
//           console.error("Error parsing token response:", ex);
//           console.error("Raw response:", this.responseText);
//           return;
//         }

//         const payload = JSON.stringify({
//           input_data: [{
//             fields: ['Age','Sex','ChestPainType','RestingBP','Cholesterol','FastingBS','RestingECG','MaxHR','ExerciseAngina','Oldpeak','ST_Slope'],
//             values: [
//               [age,sex,cpt,rbp,chl,fbs,recg,mhr,eang,op,st]
//             ]
//           }]
//         });

//         const scoring_url = "http://localhost:3000/api/scoring";

//         apiPost(scoring_url, tokenResponse.access_token, payload,
//           function () {
//             let parsedPostResponse;
//             try {
//               parsedPostResponse = JSON.parse(this.responseText);
//             } catch (ex) {
//               console.error("Error parsing scoring response:", ex);
//               console.error("Raw response:", this.responseText);
//               return;
//             }
//             console.log("Scoring response:");
//             console.log(parsedPostResponse);
//           },
//           function (error) {
//             console.error("Error in API call:", error);
//           }
//         );
//       }
//     );
//   });
