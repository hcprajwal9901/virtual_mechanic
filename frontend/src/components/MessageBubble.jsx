import React from 'react'

export default function MessageBubble({ role, text }){
  const isUser = role === 'user'
  return (
    <div style={{display:'flex', justifyContent: isUser ? 'flex-end' : 'flex-start'}}>
      <div style={{
        background: isUser ? '#4361ee' : '#1b2559',
        color:'#fff',
        padding:'10px 14px',
        borderRadius:12,
        maxWidth:'80%'
      }}>
        <pre style={{margin:0, whiteSpace:'pre-wrap', fontFamily:'inherit'}}>{text}</pre>
      </div>
    </div>
  )
}
