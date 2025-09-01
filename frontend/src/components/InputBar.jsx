import React, { useState } from 'react'

export default function InputBar({ onSend }){
  const [value, setValue] = useState('My car won\'t start, I hear clicking')

  const submit = (e) => {
    e.preventDefault()
    if (!value.trim()) return
    onSend(value.trim())
    setValue('')
  }

  return (
    <form onSubmit={submit} style={{display:'flex', gap:8, padding:12}}>
      <input
        value={value}
        onChange={e=>setValue(e.target.value)}
        placeholder="Describe a symptom or type: maintenance / tips"
        style={{flex:1, padding:'12px 14px', borderRadius:10, border:'1px solid #2a345d', background:'#0b1020', color:'#e9eefb'}}
      />
      <button type="submit" style={{padding:'0 18px', borderRadius:10, border:'none', background:'#00c853', color:'#05210f', fontWeight:700}}>Send</button>
    </form>
  )
}
