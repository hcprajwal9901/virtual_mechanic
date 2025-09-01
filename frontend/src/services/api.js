const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000'


export async function diagnose(payload) {
const res = await fetch(`${API_BASE}/api/v1/diagnostics/diagnose`, {
method: 'POST',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify(payload)
})
if (!res.ok) throw new Error('Diagnosis failed')
return res.json()
}


export async function maintenance(payload) {
const res = await fetch(`${API_BASE}/api/v1/maintenance/due`, {
method: 'POST',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify(payload)
})
if (!res.ok) throw new Error('Maintenance fetch failed')
return res.json()
}


export async function tips(payload) {
const res = await fetch(`${API_BASE}/api/v1/tips/suggest`, {
method: 'POST',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify(payload)
})
if (!res.ok) throw new Error('Tips fetch failed')
return res.json()
}