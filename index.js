const form = document.querySelector('#userReq');
const topicList = document.querySelector('#topics');

form.addEventListener("submit", async e => {
    e.preventDefault();
    const formData = new FormData(form);

    const data = {
        subject: formData.get("subject"),
        goal: formData.get("goal"),
        weeks: Number(formData.get("weeks")),
        length: Number(formData.get("length"))
    }

    const response = await fetch("http://127.0.0.1:8000/syllabus", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    result.forEach(text => {
    const week = document.createElement('li');
    week.textContent = text; 
    topicList.appendChild(week); 
    });
})