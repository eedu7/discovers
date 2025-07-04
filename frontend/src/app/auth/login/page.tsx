import React from "react";
import { Metadata } from "next";

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";
import { LoginForm } from "@/app/auth/_components/LoginForm";
import { LoginRegisterCardFooter } from "@/app/auth/_components/LoginRegisterCardFooter";

export const metadata: Metadata = {
    title: "Discover | Log In",
    description: "Discover | Log In",
};

function LoginPage() {
    return (
        <div className="grid place-content-center">
            <Card className="w-full min-w-[300px] md:w-md">
                <CardHeader>
                    <CardTitle>Log In</CardTitle>
                </CardHeader>
                <CardContent>
                    <LoginForm />
                </CardContent>
                <Separator />
                <LoginRegisterCardFooter />
            </Card>
        </div>
    );
}

export default LoginPage;
