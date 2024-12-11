import { Terminal } from './components/Terminal'

function App() {
  return (
    <div style={{ 
      height: '100vh',
      width: '100vw',
      backgroundColor: '#000000',
      margin: 0,
      padding: 0,
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center'
    }}>
      <div style={{
        width: '80%',
        height: '80%',
        maxWidth: '1200px',
        maxHeight: '800px',
        border: '1px solid #33ff33',
        borderRadius: '4px',
        overflow: 'hidden'
      }}>
        <Terminal />
      </div>
    </div>
  )
}

export default App
