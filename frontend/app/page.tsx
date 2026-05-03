import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

export default function Home() {
  return (
    <main className="min-h-screen flex items-center justify-center p-8">
      <div className="max-w-md w-full space-y-8">
        
        {/* Testing Fonts and Colors */}
        <div className="text-center">
          <h1 className="text-4xl font-extrabold mb-2 text-primary">
            OpportuAI Test
          </h1>
          <p className="text-secondary-foreground font-mono">
            If you can read this, fonts are working.
          </p>
        </div>

        {/* Testing Components */}
        <Card>
          <CardHeader>
            <CardTitle className="flex justify-between items-center">
              <span>Test Card</span>
              <Badge>Strong Match 🟢</Badge>
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <Input placeholder="Type a skill here..." />
            <Button className="w-full">
              Find My Matches &rarr;
            </Button>
          </CardContent>
        </Card>

      </div>
    </main>
  );
}