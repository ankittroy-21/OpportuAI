import { Plus_Jakarta_Sans, Inter, JetBrains_Mono } from "next/font/google";
import "./globals.css";
import { Geist } from "next/font/google";
import { cn } from "@/lib/utils";

const geist = Geist({subsets:['latin'],variable:'--font-sans'});

const jakarta = Plus_Jakarta_Sans({ 
  subsets: ["latin"], 
  variable: "--font-jakarta" 
});

const inter = Inter({ 
  subsets: ["latin"], 
  variable: "--font-inter" 
});

const jetbrains = JetBrains_Mono({ 
  subsets: ["latin"], 
  variable: "--font-mono" 
});

export const metadata = {
  title: "OpportuAI | Your Career Companion",
  description: "AI-powered opportunity matching platform for students.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={`${inter.className} ${jakarta.variable} ${jetbrains.variable} antialiased`}>
    <html lang="en" className={cn("font-sans", geist.variable)}>
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}