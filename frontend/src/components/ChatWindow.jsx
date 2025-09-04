import React, { useState } from 'react'
import MessageBubble from './MessageBubble'
import InputBar from './InputBar'
import { diagnose, maintenance, tips } from '../services/api'

const defaultVehicle = {
  make: 'Honda',
  model: 'Accord',
  year: 2020,
  fuel_type: 'petrol'
}

export default function ChatWindow(){
  const [messages, setMessages] = useState([
    {role:'bot', text: 'Hi! I\'m your Virtual Mechanic. Tell me a symptom or ask for maintenance/tips.'}
  ])
  const [vehicle, setVehicle] = useState(defaultVehicle)
  const [odo, setOdo] = useState(41200)

  const send = async (text) => {
    setMessages(m => [...m, {role:'user', text}])

    const lower = text.toLowerCase()

    try {
      if (lower.includes('maint') || lower.includes('service')) {
        const data = await maintenance({ vehicle, odometer_km: odo })
        const lines = data.items.slice(0,6).map(i=>`• ${i.task} — ${i.status} (every ${i.interval_km} km)`).join('\n')
        setMessages(m => [...m, {role:'bot', text: `Maintenance for ${vehicle.make} ${vehicle.model} @ ${odo} km:\n${lines}` }])
        return
      }

      if (lower.includes('tip')) {
        const data = await tips({ vehicle, context: 'general' })
        const lines = data.tips.map(t=>`• ${t.title}: ${t.detail}`).join('\n')
        setMessages(m => [...m, {role:'bot', text: `Here are some tips:\n${lines}` }])
        return
      }

      // default → diagnose
      const data = await diagnose({ vehicle, odometer_km: odo, description: text })
      const lines = data.top_candidates.map(c=>`• ${c.issue} — ${(c.confidence*100).toFixed(0)}%\n  Next: ${c.next_steps}`).join('\n')
      setMessages(m => [...m, {role:'bot', text: `Possible causes:\n${lines}` }])

    } catch (e) {
      setMessages(m => [...m, {role:'bot', text: `Oops, something went wrong: ${e.message}` }])
    }
  }

  return (
    <div style={{width: 'min(720px, 96vw)', height:'80vh', background:'#101936', color:'#e9eefb', borderRadius:16, display:'flex', flexDirection:'column', boxShadow:'0 10px 30px rgba(0,0,0,0.4)'}}>
      <div style={{padding:'16px 20px', borderBottom:'1px solid #2a345d', display:'flex', alignItems:'center', gap:12}}>
        <div style={{fontWeight:700, fontSize:18}}>Virtual Mechanic</div>
        <div style={{marginLeft:'auto', fontSize:12, opacity:0.8}}>
          Vehicle:&nbsp;
          <select value={vehicle.make} onChange={e=>setVehicle(v=>({...v, make:e.target.value}))}>
            <option>Honda</option>
            <option>Toyota</option>
            <option>Tata</option>
            <option>Hyundai</option>
          </select>
          &nbsp;
          <input value={vehicle.model} onChange={e=>setVehicle(v=>({...v, model:e.target.value}))} style={{width:90}} />
          &nbsp;
          <input type="number" value={vehicle.year} onChange={e=>setVehicle(v=>({...v, year:Number(e.target.value)}))} style={{width:70}} />
          &nbsp;
          <select value={vehicle.fuel_type} onChange={e=>setVehicle(v=>({...v, fuel_type:e.target.value}))}>
            <option value="petrol">petrol</option>
            <option value="diesel">diesel</option>
            <option value="electric">electric</option>
            <option value="hybrid">hybrid</option>
            <option value="cng">cng</option>
            <option value="lpg">lpg</option>
          </select>
          &nbsp;·&nbsp;
          Odo:&nbsp;
          <input type="number" value={odo} onChange={e=>setOdo(Number(e.target.value))} style={{width:90}} /> km
        </div>
      </div>

      <div style={{flex:1, overflowY:'auto', padding:16, display:'flex', flexDirection:'column', gap:10}}>
        {messages.map((m, i) => <MessageBubble key={i} role={m.role} text={m.text} />)}
      </div>

      <div style={{borderTop:'1px solid #f01919b9'}}>
        <InputBar onSend={send} />
      </div>
    </div>
  )
}
