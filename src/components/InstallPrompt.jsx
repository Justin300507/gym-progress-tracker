import React, { useState, useEffect } from 'react';
import { Download, X } from 'lucide-react';

const InstallPrompt = () => {
  const [prompt, setPrompt] = useState(null);
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const handler = (e) => { e.preventDefault(); setPrompt(e); setVisible(true); };
    window.addEventListener('beforeinstallprompt', handler);
    return () => window.removeEventListener('beforeinstallprompt', handler);
  }, []);

  const install = async () => {
    if (!prompt) return;
    prompt.prompt();
    const { outcome } = await prompt.userChoice;
    if (outcome === 'accepted') setVisible(false);
  };

  if (!visible) return null;

  return (
    <div className="fixed bottom-4 left-4 right-4 sm:left-auto sm:right-4 sm:w-80 bg-indigo-600 text-white rounded-xl shadow-xl p-4 flex items-start gap-3 z-50 animate-in slide-in-from-bottom-4">
      <div className="flex-1">
        <p className="font-semibold text-sm">Install App</p>
        <p className="text-xs text-indigo-200 mt-0.5">Add to your home screen for the best experience.</p>
        <div className="flex gap-2 mt-3">
          <button onClick={install} className="flex items-center gap-1.5 bg-white text-indigo-700 text-xs font-semibold px-3 py-1.5 rounded-lg hover:bg-indigo-50 transition-colors">
            <Download size={13} /> Install
          </button>
          <button onClick={() => setVisible(false)} className="text-xs text-indigo-200 hover:text-white px-2 py-1.5 rounded-lg hover:bg-indigo-700 transition-colors">
            Not now
          </button>
        </div>
      </div>
      <button onClick={() => setVisible(false)} className="text-indigo-300 hover:text-white mt-0.5">
        <X size={16} />
      </button>
    </div>
  );
};

export default InstallPrompt;
