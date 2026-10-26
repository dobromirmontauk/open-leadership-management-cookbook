import type { Metadata } from 'next';
import './globals.css';
export const metadata:Metadata={title:'Good Manager / Great Manager',description:'A shared language for growth. Scorecard-driven leadership workshops and peer feedback.',referrer:'no-referrer'};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="en"><body>{children}</body></html>}
