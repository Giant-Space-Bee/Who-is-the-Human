import { Link } from 'react-router-dom';

export function HomePage() {
  return (
    <div style={{
      height: '100vh',
      width: '100vw',
      backgroundColor: '#000000',
      color: '#33ff33',
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      gap: '2rem',
      fontFamily: 'Menlo, Monaco, "Courier New", monospace',
    }}>
      <h1 style={{ fontSize: '2.5rem', textAlign: 'center' }}>
        POOCS: The Human
      </h1>
      <p style={{ fontSize: '1.2rem', maxWidth: '600px', textAlign: 'center' }}>
        A social deception game where AI players try to identify the human among them.
      </p>
      <Link 
        to="/game" 
        style={{
          padding: '1rem 2rem',
          border: '2px solid #33ff33',
          borderRadius: '4px',
          color: '#33ff33',
          textDecoration: 'none',
          fontSize: '1.2rem',
          transition: 'all 0.3s ease',
        }}
        onMouseOver={(e) => {
          e.currentTarget.style.backgroundColor = '#33ff33';
          e.currentTarget.style.color = '#000000';
        }}
        onMouseOut={(e) => {
          e.currentTarget.style.backgroundColor = 'transparent';
          e.currentTarget.style.color = '#33ff33';
        }}
      >
        Start Game
      </Link>
    </div>
  );
} 