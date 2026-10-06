document.querySelectorAll('.yr,#yr').forEach(el=>el.textContent=new Date().getFullYear());
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
const hdr=document.querySelector('header');
addEventListener('scroll',()=>hdr&&hdr.classList.toggle('scrolled',scrollY>10));
document.querySelectorAll('.links a').forEach(a=>a.addEventListener('click',()=>document.getElementById('links').classList.remove('open')));
document.querySelectorAll('.svc details').forEach(d=>d.addEventListener('toggle',()=>{if(d.open)document.querySelectorAll('.svc details').forEach(o=>{if(o!==d)o.open=false})}));
// ---- Lead forms → GoHighLevel ----
// Paste the URL from your GHL workflow's "Inbound Webhook" trigger below.
const GHL_WEBHOOK_URL = "";
document.querySelectorAll('form.lead-form, form#lead').forEach(f=>f.addEventListener('submit',async e=>{
  e.preventDefault();
  const fd=new FormData(f), data={};
  fd.forEach((v,k)=>{ data[k] = data[k] ? data[k]+', '+v : v; });
  if(data.first||data.last) data.name=[data.first,data.last].filter(Boolean).join(' ');
  data.area = data.area || 'Website (homepage)';
  data.service = data.service || data.need || 'Not specified';
  data.page = location.pathname; data.source = 'MindSync website';
  const btn=f.querySelector('button[type=submit]'); if(btn){btn.disabled=true;btn.textContent='Sending…';}
  try{ if(GHL_WEBHOOK_URL) await fetch(GHL_WEBHOOK_URL,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)}); }
  catch(err){ console.error('Lead submit failed',err); }
  const ok=f.querySelector('.ok'); if(ok) ok.style.display='block';
  if(btn){btn.disabled=false;btn.textContent='Send →';}
  f.reset();
}));
