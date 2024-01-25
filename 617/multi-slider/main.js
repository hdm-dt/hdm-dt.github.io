const slider1 = document.querySelector(".image-comparison .slider2");
const contentImage1 = document.querySelector(".image-comparison .image2");
const sliderLine1 = document.querySelector(".image-comparison .slider-line2");
 
const sliderButton1 = document.querySelector(".image-comparison .slider-button2");
 
slider1.addEventListener("input", (e) => {
  let sliderValue = e.target.value + "%";
 
  contentImage1.style.width = sliderValue;
  sliderLine1.style.left = sliderValue;
 
  sliderButton1.style.left = sliderValue;
});
 
const slider2 = document.querySelector(".image-comparison .slider1");
const contentImage2 = document.querySelector(".image-comparison .image1");
const sliderLine2 = document.querySelector(".image-comparison .slider-line1");
 
const sliderButton2 = document.querySelector(".image-comparison .slider-button1");
 
slider2.addEventListener("input", (e) => {
  let sliderValue = e.target.value + "%";
 
  contentImage2.style.width = sliderValue;
  sliderLine2.style.left = sliderValue;
 
  sliderButton2.style.left = sliderValue;
});
 
const slider3 = document.querySelector(".image-comparison .slider3");
const contentImage3 = document.querySelector(".image-comparison .image3");
const sliderLine3 = document.querySelector(".image-comparison .slider-line3");
 
const sliderButton3 = document.querySelector(".image-comparison .slider-button3");
 
slider3.addEventListener("input", (e) => {
  let sliderValue = e.target.value + "%";
 
  contentImage3.style.width = sliderValue;
  sliderLine3.style.left = sliderValue;
 
  sliderButton3.style.left = sliderValue;
});
 
const slider4 = document.querySelector(".image-comparison .slider4");
const contentImage4 = document.querySelector(".image-comparison .image4");
const sliderLine4 = document.querySelector(".image-comparison .slider-line4");
 
const sliderButton4 = document.querySelector(".image-comparison .slider-button4");
 
slider4.addEventListener("input", (e) => {
  let sliderValue = e.target.value + "%";
 
  contentImage4.style.width = sliderValue;
  sliderLine4.style.left = sliderValue;
 
  sliderButton4.style.left = sliderValue;
});

const slider5 = document.querySelector(".image-comparison .slider5");
const contentImage5 = document.querySelector(".image-comparison .image5");
const sliderLine5 = document.querySelector(".image-comparison .slider-line5");
 
const sliderButton5 = document.querySelector(".image-comparison .slider-button5");
 
slider5.addEventListener("input", (e) => {
  let sliderValue = e.target.value + "%";
 
  contentImage5.style.width = sliderValue;
  sliderLine5.style.left = sliderValue;
 
  sliderButton5.style.left = sliderValue;
});

