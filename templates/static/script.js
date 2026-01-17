<script>
window.onload = function() {
  // 1 Get variables from Flask
  let score = {{ score | tojson }};
  let riskLevel = {{ risk_level | tojson }};
  let verdict = {{ verdict | tojson }};
  let companyStatus = {{ company_status | tojson }};
  let detectedHigh = {{ detected_high | tojson }};
  let detectedMedium = {{ detected_medium | tojson }};
  let jobTextRaw = {{ job_text | tojson }};

  // 2 DOM Elements
  let trustScore = document.getElementById("trustScore");
  let trustLabel = document.getElementById("trustLabel");
  let circle = document.getElementById("progressCircle");

  // 3 Circular progress animation
  let radius = 70;
  let circumference = 2 * Math.PI * radius;
  circle.style.strokeDasharray = circumference;
  circle.style.strokeDashoffset = circumference;

  let offset = circumference * (1 - score / 100);
  setTimeout(() => { circle.style.strokeDashoffset = offset; }, 100);

  // 4 Color based on riskLevel
  if (riskLevel === "High Risk") circle.style.stroke = "#dc2626";
  else if (riskLevel === "Medium Risk") circle.style.stroke = "#facc15";
  else circle.style.stroke = "#16a34a";

  trustScore.innerText = score + "%";
  trustLabel.innerText = riskLevel;

  // 5️⃣ Table: Keywords Check & Job Type Risk
  let keywordsStatus = detectedHigh.length > 0 ? "High Risk" :
                       detectedMedium.length > 0 ? "Medium Risk" : "Low Risk";
  let jobTypeStatus = keywordsStatus;

  document.getElementById("keywordsStatus").innerText = keywordsStatus;
  document.getElementById("companyStatus").innerText = companyStatus;
  document.getElementById("jobTypeStatus").innerText = jobTypeStatus;

  // 6 Verdict
  document.getElementById("verdictText").innerText = verdict;

  // 7 Highlight suspicious keywords in job description
  let highlightedText = jobTextRaw;
  detectedHigh.forEach(k => {
    let re = new RegExp(`(${k})`, "gi");
    highlightedText = highlightedText.replace(re, `<span class="keyword-high">$1</span>`);
  });
  detectedMedium.forEach(k => {
    let re = new RegExp(`(${k})`, "gi");
    highlightedText = highlightedText.replace(re, `<span class="keyword-medium">$1</span>`);
  });
  document.getElementById("jobText").innerHTML = highlightedText;

  // 8 Suspicious keywords badges
  let allDetected = detectedHigh.concat(detectedMedium);
  if(allDetected.length > 0){
    document.getElementById("suspiciousKeywords").innerHTML = 
      allDetected.map(k => `<span class="badge ${detectedHigh.includes(k) ? 'bg-danger' : 'bg-warning text-dark'}">${k}</span>`).join(' ');
  } else {
    document.getElementById("suspiciousKeywords").innerText = "None";
  }
};
</script>

</body>
</html>
