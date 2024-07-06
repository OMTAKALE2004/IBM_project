let t1 = gsap.timeline();
let t2 = gsap.timeline();
t1.from('#logo',{
  y:"-20vh",
  delay:'100ms',
  scale:0
}) 
t1.from('h2',{
  y:'60vh',
  
})
t1.from('.button',{
  scale:0,
  delay:'100ms'
})

t2.from("#doc",{
  x:"60vw",
  scale:0,
  delay:"100ms"
})
t2.from('#name',{
  y:"-20vh"
})