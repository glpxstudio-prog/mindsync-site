document.querySelectorAll('.yr,#yr').forEach(el=>el.textContent=new Date().getFullYear());
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
const hdr=document.querySelector('header');
addEventListener('scroll',()=>hdr&&hdr.classList.toggle('scrolled',scrollY>10));
document.querySelectorAll('.links a').forEach(a=>a.addEventListener('click',()=>document.getElementById('links').classList.remove('open')));
document.querySelectorAll('.svc details').forEach(d=>d.addEventListener('toggle',()=>{if(d.open)document.querySelectorAll('.svc details').forEach(o=>{if(o!==d)o.open=false})}));
// Demo submit — replace with your CRM inbound webhook (e.g. GoHighLevel). Hidden fields "area" and "service" tag each lead.
document.querySelectorAll('form.lead-form, form#lead').forEach(f=>f.addEventListener('submit',e=>{e.preventDefault();const ok=f.querySelector('.ok');if(ok)ok.style.display='block';f.reset();}));
