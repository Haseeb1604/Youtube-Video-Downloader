const $ = selector => document.querySelector(selector);
let toggleFormBtn = (downloadbtn, loadbtn, load=true) => {
  if(load){
    downloadbtn.style.display = "none";
    loadbtn.style.display = "block";
  }else{
    loadbtn.style.display = "none";
    downloadbtn.style.display = "block";
  }
}

const main = () => {
  const youtubeForm = $("#youtubeForm");
  const downloadform = $("#downloadForm");

  // const downloadBtn = $('#download_btn');
  // const download_loadingBtn = $('#loading_btn');

  // if(downloadBtn){
  //   downloadBtn.addEventListener('click', () =>{
  //     toggleFormBtn(downloadBtn, download_loadingBtn);
  //   })
  // }

  // YouTube Form submission event
  youtubeForm.addEventListener('submit', (e) => {
    e.preventDefault();
    let formData = new FormData(youtubeForm);
    // Sending form data throught ajax POST request
    ajax({
      url: "/youtube",
      method: "POST",
      data: formData,
      // while the submission process is still in progress we will show loading button instead of download
      onprogress: () => {
        toggleFormBtn($('#youtube_download_btn'),$('#youtube_loading_btn'), true)
      },  
      // Successful submission 
      onsuccess: (response) => {
        // showing download btn and hiding loading indicator
        toggleFormBtn($('#youtube_download_btn'),$('#youtube_loading_btn'), false)

        // Converting to response to js object
        response = JSON.parse(response);
        // if response has url its mean there is no error
        if (response.url) {
          // assigning appropriate values for download form data
          downloadform.style.display = "block";
          downloadform.querySelector('.thumbnail_img').src = response.url;
          downloadform.querySelector('.card-title').innerHTML = response.title;
          for (const [key, item] of Object.entries(response.stream))
            downloadform.querySelector('.form-select').innerHTML += `
              <option value="${key}"> ${item} </option>
              `;
        } else {
          // if response doesnt has url then its mean there is an error so displaying error box
          $('#alert-box').style.display = 'block';
          $('#alert-box span').innerHTML = response.error;
        }
      },
      
      onfailure: (status, statusText) => {
        toggleFormBtn($('#youtube_download_btn'),$('#youtube_loading_btn'), false)
        $('#alert-box').style.display = 'block';
        $('#alert-box span').innerHTML = `${status} ${statusText}! Something went wrong`;
      }
    })
  })

  // Download form submission
  // downloadform.addEventListener('submit', e => {
  //   e.preventDefault();

  //   let formData = new FormData(downloadform);
  //   ajax({
  //     url: '/download',
  //     method: "POST",
  //     data: formData,
  //     onprogress: (data) => {
  //       console.log(data);
  //       toggleFormBtn(downloadBtn,download_loadingBtn, true)
  //     },
  //     onsuccess: (response, status, statusText) => {
  //       console.log(status, statusText);
  //       console.log(response);
  //       toggleFormBtn(downloadBtn,download_loadingBtn, false)
  //     },
  //     onfailure: (data, status) => {
  //       console.log(data, status);
  //       toggleFormBtn(downloadBtn,download_loadingBtn, false)
  //     }
  //   })
  
  // })

}

window.onload = () => main();