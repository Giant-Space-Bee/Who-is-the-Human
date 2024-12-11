import { useEffect, useRef } from 'react';
import { Terminal as XTerm } from '@xterm/xterm';
import { FitAddon } from '@xterm/addon-fit';
import '@xterm/xterm/css/xterm.css';

export function Terminal() {
  const terminalRef = useRef<HTMLDivElement>(null);
  const xtermRef = useRef<XTerm | null>(null);
  const fitAddonRef = useRef<FitAddon | null>(null);

  useEffect(() => {
    const initTerminal = async () => {
      if (!terminalRef.current || xtermRef.current) return;

      try {
        // Create terminal instance
        const term = new XTerm({
          cursorBlink: true,
          theme: {
            background: '#000000',
            foreground: '#33ff33',
            cursor: '#33ff33',
          },
          fontFamily: 'Menlo, Monaco, "Courier New", monospace',
          fontSize: 14,
          convertEol: true,
          allowTransparency: true,
        });

        // Create and load fit addon
        const fitAddon = new FitAddon();
        term.loadAddon(fitAddon);

        // Store references first
        xtermRef.current = term;
        fitAddonRef.current = fitAddon;

        // Open terminal in container
        term.open(terminalRef.current);

        // Initial fit
        fitAddon.fit();

        // Write welcome message
        term.write('\x1b[32m=== POOCS: The Human ===\x1b[0m\r\n');
        term.write('Welcome to the game! Terminal initialized...\r\n\r\n');

        // Handle window resize
        const handleResize = () => fitAddon.fit();
        window.addEventListener('resize', handleResize);

        // Return cleanup function
        return () => {
          window.removeEventListener('resize', handleResize);
          term.dispose();
        };
      } catch (error) {
        console.error('Terminal initialization error:', error);
      }
    };

    initTerminal();
  }, []);

  return (
    <div 
      ref={terminalRef}
      style={{
        height: '100%',
        width: '100%',
        backgroundColor: '#000000',
      }}
    />
  );
} 