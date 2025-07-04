import React from "react";
import { Metadata } from "next";

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";
import { LoginRegisterCardFooter } from "@/app/auth/_components/LoginRegisterCardFooter";
import { RegisterForm } from "@/app/auth/_components/RegisterForm";

export const metadata: Metadata = {
    title: "Discover | Register",
    description: "Discover | Register",
};

function RegisterPage() {
    return (
        <div className="grid place-content-center px-2 md:px-0">
            <Card className="w-full md:w-md">
                <CardHeader className="text-center">
                    <CardTitle className="text-lg">Create Your Discover Account</CardTitle>
                    <CardDescription className="italic">
                        Shop your favorite products and manage orders with ease.
                    </CardDescription>
                </CardHeader>
                <CardContent>
                    <RegisterForm />
                </CardContent>
                <Separator />
                <LoginRegisterCardFooter />
            </Card>
        </div>
    );
}

export default RegisterPage;
